# cascade
Ik. Im pretty awesome. A functioning coding language that uses python as a compiler. run the file and get access to a little IDE and terminal.
Cascade is a unique programming language with a flowing, waterfall-like syntax designed for simplicity and readability.

## Syntax Dictionary

### Variable Assignment
- Syntax: `variable_name ~> expression`
- Example: `x ~> 5`
- Description: Assigns the result of the expression to the variable name.

### Printing
- Syntax: `>> expression`
- Example: `>> x + 10`
- Description: Evaluates the expression and prints the result to the output.

### Arithmetic Operations
- Supported operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division)
- Example: `result ~> (x + y) * 2`

### Variable Usage
- Variables can be used in expressions once defined
- Example: 

Copy

Apply

x ~> 5 y ~> x * 2

y # Outputs 10


### Multiple Operations
- Multiple operations can be performed in a single expression
- Example: `total ~> a + b + c * d / e`

### Cascading Operations
- Operations can be cascaded using multiple lines
- Example:

Copy

Apply

x ~> 5 y ~> x + 3 z ~> y * 2

z


### Comments
- Currently not supported, but planned for future versions

## IDE Features

- Syntax highlighting (planned feature)
- Real-time error checking (planned feature)
- Integrated output display
