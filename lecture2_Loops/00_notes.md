# 🧠 CS50 Python – Lecture 2: Loops

## 🔁 while & for Loops
- `while` loop:
    ```python
    while True:
        ...
        if condition:
            break
    ```

- `for` with `range()`:
    ```python
    for i in range(5):  # 0 to 4
        print(i)
    ```

## 🔄 range() & _
- `range(n)` → 0 to n-1
- Can be used with a throwaway `_`:
    ```python
    for _ in range(3):
        print("meow")
    ```

- Other formats:
    ```python
    range(start, stop)
    range(start, stop, step)
    ```

## 🧺 Lists
- Ordered, mutable, heterogenous:
    ```python
    items = [1, "hello", 3.14]
    print(items[1])          # "hello"
    items.append("new")
    print(len(items))        # 4
    ```

## 🗃️ Dictionaries
- Key-value pairs (mutable, ordered):
    ```python
    info = {"name": "Alice", "age": 30}
    print(info["name"])
    info["city"] = "Delhi"
    ```

## 🈳 `None`
- Special null-like value:
    ```python
    x = None
    if x is None:
        print("x is None")
    ```
