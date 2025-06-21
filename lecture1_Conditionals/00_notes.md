# 🧠 CS50 Python – Lecture 1: Conditionals

## ⚖️ Boolean Expressions
- Operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Used with `if`, `while`, etc.
- Return `True` or `False`

## 🔁 if / elif / else
- Syntax:
    ```python
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
    ```

- Combine with `and`, `or`
- Chain comparisons: `90 <= score < 100`
- One-liner:
    ```python
    print("Even") if x % 2 == 0 else print("Odd")
    ```

## 🎯 `match` Statement (Python 3.10+)
- Switch-case alternative:
    ```python
    match name:
        case "Alice":
            ...
        case "Bob":
            ...
        case _:
            ...
    ```

- Use `|` for multiple matches:
    ```python
    case "yes" | "y":
        ...
    ```

## 💡 String Methods from Practice

### `.lower()`
- Case-insensitive input handling:
    ```python
    name = input().lower()
    ```

### `.startswith()` and `.endswith()`
- Prefix/suffix checks:
    ```python
    text.startswith(("Hi", "Hey"))
    file.endswith(".png")
    ```

### `.removesuffix()`
- Removes a suffix if present:
    ```python
    "hello.py".removesuffix(".py")  # "hello"
    ```

### `.split()`
- Splits string into parts:
    ```python
    x, y, z = "7 + 3".split()  # x='7', y='+', z='3'
    ```
