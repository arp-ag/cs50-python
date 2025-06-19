# CS50 Python – Lecture 0 Notes
- Can use double or single quotes.
## 🖨️ Output
- Syntax: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
- `print("Hello" + name)` concatenates, thus no space in between.
- `print("Hello ", name)` displays separately, automatic space in between.
- `print(f"Hello {name}")` is good to use! Eg: displays 100,000,000.00 (number formatted automatically)

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