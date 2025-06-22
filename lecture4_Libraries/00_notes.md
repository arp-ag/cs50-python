# 📚 CS50 Python – Lecture 4: Libraries & Packages

## 📖 What Are Libraries?
- Reusable code collections (functions, classes, variables).
- Python includes built-in libraries (e.g., `math`, `random`, `sys`).
- Third-party libraries can be installed via `pip`.

---

## 📦 Importing Modules
- `import module`
- `import module as alias`
- `from module import function`

---

## 🎲 `random` Module (built-in)
- `random.choice(list)` → random element
- `random.randint(a, b)` → random int in range [a, b]
- `random.shuffle(list)` → shuffles list in-place

---

## 💻 `sys` Module (built-in)
- `sys.argv` → list of command-line args (`argv[0]` = filename)
- Check `len(sys.argv)` to validate input count
- `sys.exit("message")` → exit program with optional message
- Use `argv[1:]` slicing to skip filename

---

## 🧮 `statistics` Module
- `statistics.mean([a, b, c])` → returns average

---

## 🐮 `cowsay` (external)
- Fun ASCII art speech tool.
- Install: `pip install cowsay`
- `cowsay.cow("msg")`, `cowsay.trex("msg")`, etc.

---

## 📦 Creating Your Own Package
- Save custom functions in a `.py` file (e.g., `sayings.py`)
- Import in another file using:
  ```python
  from sayings import hello, goodbye
  ```
- Group related code into folders for large packages.

---

## 🌐 APIs & `requests` (external)
- Install: `pip install requests`
- `requests.get(url)` → makes HTTP GET request
- `.json()` → parses response as a dictionary
- `json.dumps(obj, indent=n)` → pretty-print JSON

---

## 🔍 `__name__` and `__main__`
- `__name__` is `"__main__"` only when a file is run directly.
- Use:
  ```python
  if __name__ == "__main__":
      main()
  ```
- Prevents code from running when module is imported.