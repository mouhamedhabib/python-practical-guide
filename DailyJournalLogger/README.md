# 🔹 File Writing in Python

This section explains how file writing works in Python, how to handle file modes safely, manage errors, and includes a practical project: **Daily Journal Logger**.

---

## ❓ What is File Writing in Python?

Python provides built-in functions to write data to files using the `open()` function.

### Basic Syntax:

```python
open(filename, mode)
```

Common modes:

| Mode | Description |
|------|------------|
| `"w"` | Write mode (creates or overwrites file) |
| `"a"` | Append mode (adds content without deleting existing data) |
| `"r"` | Read mode |
| `"r+"` | Read and write |

📌 Important:
- `"w"` overwrites existing content.
- `"a"` keeps existing content and adds new data at the end.

---

## 🔹 Writing to Files (`w` mode)

```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")
```

Using `with` ensures:
- The file closes automatically
- Resources are properly managed
- No memory leaks

---

## 🔹 Appending to Files (`a` mode)

```python
with open("example.txt", "a") as file:
    file.write("This line will be appended to the file.\n")
```

This adds content without deleting existing text.

---

## 🔹 Handling File Writing Errors

File operations may raise exceptions such as:
- `FileNotFoundError`
- `PermissionError`
- General system errors

Example:

```python
try:
    with open("/invalid_path/example.txt", "w") as file:
        file.write("This will raise an error.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")
```

Defensive programming = production-ready code.

---

# 🛠 Project: Daily Journal Logger

We will build a simple CLI journal system that allows:

- Adding entries
- Viewing all entries
- Searching entries by keyword

---

## Step 1: Define the Journal File

```python
JOURNAL_FILE = "daily_journal.txt"
```

---

## Step 2: Add a New Entry

```python
def add_entry():
    entry = input("Write your journal entry: ")
    with open(JOURNAL_FILE, "a") as file:
        file.write(entry + "\n")
    print("Entry added successfully!")
```

---

## Step 3: View All Entries

```python
def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Journal Entries ---")
                print(content)
            else:
                print("No entries found. Start writing today")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")
```

---

## Step 4: Search Entries by Keyword

```python
def search_entries():
    keyword = input("Enter a keyword to search for: ").lower()
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results ---")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")
```

---

## Step 5: Display Menu

```python
def show_menu():
    print("\n--- Daily Journal Logger ---")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Exit")
```

---

## Step 6: Main Program Loop

```python
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
```

---

## 📌 Learning Objectives

- Understand file modes (`w`, `a`, `r`)
- Use `with open()` safely
- Handle file-related exceptions
- Build a simple persistent CLI application
- Apply defensive programming practices

---

🚀 File handling is a foundational skill for real-world Python applications — from logging systems to data processing tools.