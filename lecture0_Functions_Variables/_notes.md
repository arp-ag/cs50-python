# CS50 Python – Lecture 0 (Functions, Variables) Notes 

## 🖨️ Output
- Syntax: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
- Can use double or single quotes.
- `print("Hello" + name)` concatenates, thus no space in between.
- `print("Hello ", name)` displays separately, automatic space in between.
- `print(f"Hello {name}")` is good to use! Eg: displays 100,000,000.00 (number formatted automatically)

- `end='\n'`, `sep=' '` can be overriden when need be.
- `sep=' '` works only when components inside print are separated by comma.
- `print("#" * 3)` format can not be overriden with `sep`.

## 🧍 Input & Variables
- Syntax: `variable = input("Optional prompt message")`
- Variables are dynamically typed (no type declaration).
- Eg: `name = input("What's your name?")`

## 🧱 Functions & Structure
- Syntax: 
    ```python
    def function_name(parameter1, parameter2, ...):
    """
    Docstring: A brief description of what the function does,
    its parameters, and what it returns.
    """
    # Function body: Code to be executed when the function is called
    # This part must be indented
    statement1
    statement2
    # ...
    return value_to_return # Optional: returns a value from the function

- a function defination should be done before it is called.
- or a main function may be created for the body, that might be called at the end of the program.

## 🧪 Python Interactive Shell (REPL (>>> prompt))

- You can run Python directly in the terminal using the interactive shell.
- To enter it, just type: `python` on Terminal

## 📝 Comments
- for single line comments(hash #) : `# I am learning python` 
- for multi line comments (three quotations; single '' or double "") :
    ```python
    ''' I am 
        writing a
        multiline comment. '''