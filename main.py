import tkinter as tk
from tkinter import scrolledtext
import re

class CascadeInterpreter:
    def __init__(self):
        self.variables = {}

    def tokenize(self, code):
        token_spec = [
            ('NUMBER', r'\d+(\.\d*)?'),
            ('FLOW', r'~>'),
            ('PRINT', r'>>'),
            ('OPERATOR', r'[+\-*/]'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
        return [
            {k: v for k, v in m.groupdict().items() if v is not None}
            for m in re.finditer(tok_regex, code)
            if m.lastgroup != 'SKIP'
        ]

    def evaluate(self, code):
        lines = code.split('\n')
        result = []
        for line_num, line in enumerate(lines, 1):
            try:
                tokens = self.tokenize(line)
                if not tokens:
                    continue
                if 'FLOW' in tokens[1]:
                    var_name = tokens[0]['IDENTIFIER']
                    expression = ''.join(t[k] for t in tokens[2:] for k in t if k != 'NEWLINE')
                    self.variables[var_name] = eval(expression, {}, self.variables)
                elif 'PRINT' in tokens[0]:
                    expression = ''.join(t[k] for t in tokens[1:] for k in t if k != 'NEWLINE')
                    result.append(str(eval(expression, {}, self.variables)))
                else:
                    raise SyntaxError("Invalid syntax")
            except Exception as e:
                result.append(f"Error on line {line_num}: {str(e)}")
        return '\n'.join(result)

class CascadeIDE:
    def __init__(self, master):
        self.master = master
        master.title("Cascade IDE")

        self.code_editor = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=15)
        self.code_editor.pack(padx=10, pady=10)

        self.run_button = tk.Button(master, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)

        self.output_terminal = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=10, state='disabled')
        self.output_terminal.pack(padx=10, pady=10)

        self.interpreter = CascadeInterpreter()

    def run_code(self):
        code = self.code_editor.get("1.0", tk.END)
        result = self.interpreter.evaluate(code)
        self.output_terminal.config(state='normal')
        self.output_terminal.delete("1.0", tk.END)
        self.output_terminal.insert(tk.END, result)
        self.output_terminal.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    cascade_ide = CascadeIDE(root)
    root.mainloop()
