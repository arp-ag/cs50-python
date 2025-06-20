# 🧠 CS50 Python – Lecture 2: Loops

## 🔁 while, for 
- `continue` : skip that iteration.
- `break` : get out of the most recent loop.

## range function, _ variable
- Syntax: `range(stop)`, `range(start, stop)`, or `range(start, stop, step)`
- Generates an immutable sequence of numbers.
-   ```python
    for _ in range(n):
        print("meow")
- contains integer values from 0 to n-1.
- Examples:
    ```python
    # range(stop)
    for i in range(5):  # Generates 0, 1, 2, 3, 4
    print(i)

    # range(start, stop)
    for i in range(2, 7):  # Generates 2, 3, 4, 5, 6
    print(i)

    # range(start, stop, step)
    for i in range(1, 10, 2):  # Generates 1, 3, 5, 7, 9
        print(i)

    for i in range(10, 0, -1):  # Generates 10, 9, 8, ..., 1
        print(i)

## list (array) [Ordered, Mutable, Heterogenous]
- Stores an ordered, mutable collection of items.
- can contain items of different data types.
- Example:
    ```python
    my_list = [1, "hello", 3.14, True]
    print(my_list[1])  # Accesses "hello"
    my_list.append(5)  # Adds 5 to the end
#### len() function
- Example: `len(my_list) # 4`

## dictionary [Ordered, Mutuable, Key-value pairs], None keyword
- Stores data in key-value pairs, maps unique keys to corresponding values.
- Example
    ```python
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    print(my_dict["name"])  # Accesses "Alice"
    my_dict["occupation"] = "Engineer"  # Adds a new key-value pair

