# 🧠 CS50 Python – Lecture 1: Conditionals

## ⚖️ Boolean Expressions
- Operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Used inside `if`, `while`, etc.
- Return `True` or `False`

## 🔁 Conditionals
- Syntax:
    ```python
    if condition1:
        ...
    elif condition2:
        ...
    else:
        ...
    ```
- Combine conditions using `and`, `or`
- Chained comparisons supported: `90 <= score < 100`
- One-liner conditionals:
    ```python
    return True if x % 2 == 0 else False
    ```

## 🎯 `match` Statement (Python 3.10+)
- Used like `switch-case`
- Syntax:
    ```python
    match expression:
        case pattern1:
            ...
        case pattern2:
            ...
        case _:
            ...  # Default case
    ```
- No `break` needed
- Use `|` for multiple matches in a case (like `case "yes" | "y":`)

## 💡 From Practice Questions

### 📌 String Methods

#### ✅ `.lower()`
- Used for case-insensitive comparison
    ```python
    name = input().lower()
    ```

#### ✅ `.startswith()`
- Syntax: `string.startswith(prefix)`
- `prefix` can be a tuple:
    ```python
    text = "Hello"
    print(text.startswith(("Hi", "Hey")))  # False
    ```
- Optional: `string.startswith(prefix, start_index)`

#### ✅ `.endswith()`
- Syntax: `string.endswith(suffix)`
    ```python
    file = "image.png"
    print(file.endswith(".png"))  # True
    ```

#### ✅ `.removesuffix()`
- Removes a suffix if it exists
    ```python
    file = "hello.py"
    print(file.removesuffix(".py"))  # "hello"
    ```

#### ✅ `.split()`
- Syntax: `string.split(separator, maxsplit)`
- Default: splits by whitespace
    ```python
    x, y, z = "7 + 3".split()  # x='7', y='+', z='3'
    ```
