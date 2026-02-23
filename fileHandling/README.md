# 📝 Note-Taking App – File Handling in Python

## 📂 File Handling in Python – Quick Recap

This section provides a clear and practical recap of **file handling in Python**, including how to read from files, write to files, and append content safely using the `with` statement.

---

## ❓ What is File Handling?

**File handling** is the process of creating, reading, writing, and updating files on a computer.

It allows programs to:
- Store data permanently  
- Retrieve saved information  
- Modify existing content  
- Manage text and binary files  

In Python, file operations are performed using the built-in `open()` function.

---

## 🔹 Opening a File

### Syntax

```python
open("filename.txt", "mode")
```

### Common Modes

| Mode | Purpose |
|------|----------|
| `r`  | Read (default mode) |
| `w`  | Write (overwrites existing content) |
| `a`  | Append (adds content without deleting old data) |
| `b`  | Binary mode (used for images, PDFs, etc.) |

**Best Practice:** Always use the `with` statement to ensure files are properly closed after use.

---

## 📖 Reading from a File

Used when you want to access stored data.

```python
with open("filename.txt", "r") as file:
    content = file.read()
    print(content)
```

- Opens the file in read mode  
- Retrieves its content  
- Automatically closes the file  

---

## ✍️ Writing to a File (Overwrite Mode)

Used when you want to replace existing content.

```python
with open("filename.txt", "w") as file:
    file.write("This will overwrite existing content.\n")
```

⚠️ **Warning:** `w` mode deletes previous content before writing new data.

---

## ➕ Appending to a File

Used when you want to add new content without deleting old data.

```python
with open("filename.txt", "a") as file:
    file.write("This line is added to the file.\n")
```

- Keeps existing content  
- Adds new data at the end  

---

## 🛠 Note-Taking App

This project is a simple **command-line Note-Taking application** designed to demonstrate file handling concepts in Python.

All notes are stored in:

```
myNotes.txt
```

---

## 🚀 Features

- Add a new note  
- View all saved notes  
- Delete all notes  
- Exit the application  

---

## 🧠 How It Works

The application:
1. Displays a menu  
2. Takes user input  
3. Uses file modes (`r`, `w`, `a`)  
4. Stores and retrieves notes from a text file  
5. Handles missing files safely using `try/except`  

---

## ▶️ How to Run

1. Make sure Python is installed.
2. Save the script as `note_app.py`.
3. Run the program:

```bash
python note_app.py
```

---

## 📌 Learning Objectives

By completing this project, you will learn:
- How to use `open()` with different file modes  
- How to work safely with the `with` statement  
- How to read and write text files  
- How to handle file-related exceptions  
- How to build a simple interactive CLI application  