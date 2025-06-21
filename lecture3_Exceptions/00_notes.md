# 🧠 CS50 Python – Lecture 3: 🚨 Exceptions

## ❗ What are Exceptions?
- Errors that occur during execution.
- Common ones: `ValueError`, `ZeroDivisionError`, `TypeError`, `FileNotFoundError`, etc.

## ✅ Try-Except Blocks
- Handle errors gracefully:
    ```python
    try:
        x = int(input("x: "))
    except ValueError:
        print("Invalid input")
    ```

## 🔁 Loop Until Valid Input
- Re-prompt using a loop with try-except:
    ```python
    while True:
        try:
            x = int(input("x: "))
            break
        except ValueError:
            print("x must be an integer")
    ```

## ⚠️ Catching Multiple Exceptions
- Can handle multiple types:
    ```python
    try:
        ...
    except (ValueError, ZeroDivisionError):
        ...
    ```

## 💡 `pass` Keyword
- Used to ignore the error silently:
    ```python
    try:
        ...
    except ValueError:
        pass
    ```

## ⛔ Raising Your Own Exceptions
- Use `raise` to manually throw errors:
    ```python
        def get_age():
        age = int(input("Age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age
    ```

## 🔙 Else & Finally
- `else` runs if no error occurs.
- `finally` always runs (even if error occurs):
    ```python
    try:
        x = 5 / 0
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print("Division worked")
    finally:
        print("Done")
    ```

## 🧠 Custom Error Handling in Python
- ✅ Step 1: define a custom error by creating a new class that inherits from Exception:
     ```python
    Copy
    Edit
    class InvalidInputError(Exception):
        """Raised when the input is invalid (like x > y in a fraction)"""
        pass
    ```
    
    - You can optionally define your own `__init__` and error message too:
    ```python
    class InvalidInputError(Exception):
        def __init__(self, message="Invalid input"):
            self.message = message
            super().__init__(self.message)
    ```
- ✅ Step 2: Raise the Exception Where Needed
    - "throw" the custom exception using raise:

    ```python
    x, y = map(int, input("Fraction: ").split("/"))
    if x > y:
        raise InvalidInputError("Numerator cannot be greater than denominator")
    ```
- ✅ Step 3: Catch the Custom Exception
    ```python
    try:
        ...
    except InvalidInputError as e:
        print(e)
    ```

## 🧭 map()
- Applies a given function to every item in an iterable (like a list, tuple, or string split result) and returns a lazy iterator.
    ```python
    nums = list(map(int, ["1", "2", "3"]))  # [1, 2, 3]
    ```
- Applies the **same transformation** to all elements.
- Only supports **one iterable** at a time.
- Returns a `<map object>` unless explicitly converted.