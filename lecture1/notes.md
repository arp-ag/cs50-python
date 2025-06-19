# CS50 Python – Lecture 1 (Conditionals) Notes

# 🧠 CS50 Python – Lecture 1 Notes

## ⚖️ Boolean Expressions
- `==`, `!=`, `<`, `>`, `<=`, `>=`
- Used in `if`, `while`, etc.
- Evaluate to `True` or `False`

## 🔁 Conditionals
- Syntax:
    ```python
    if condition1:
        # Code for condition1
    elif condition2:
        # Code for condition2
    else:
        # Code to execute if all preceding conditions are False
- use 'or', 'and' to compare multiple conditions.
- supports conditions like `90 <= score < 100`
- can write: `return True if x%2==0 else False`

## 🎯 Match Statement (Python 3.10+)
- Syntax:
    ```python
    match expression: #expression = variable
    case pattern1: #pattern1 = variable_value
        # code block 1
    case pattern2:
        # code block 2
    # ...
    case _:  # Optional: default case (wildcard)
        # default code block
- match...case keyword (similar to Switch...case)
- No break statement needed. No default (instead case _: )
- use single | for or 

## 💡 From the practice questions
- used .lower() for case-insensitivity (in deep.py)
- used .startswith() (in bank.py)
#### .startswith(), .endswith(), .removesuffix()
Syntax: 
- `string.startswith(prefix, start, end)`
    prefix may be a tuple eg:
    ```python
    text = "Hello, world!"
    print(text.startswith(("Hi", "Hey"))) # False
- `string.endswith(suffix, start, end)`
- `string.removesuffix(suffix)`
#### .split()
Syntax:
- `string.split(separator, maxsplit)`