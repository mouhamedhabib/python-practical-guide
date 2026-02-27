# 🔹 Working with JSON Files in Python

This section explains what JSON files are, how to read, write, and modify JSON data in Python, and includes a practical project: **Mini To-Do App using JSON**.

---

## ❓ What are JSON Files?

**JSON (JavaScript Object Notation)** is a lightweight data format used for storing and exchanging data.

It is:
- Human-readable  
- Easy for machines to parse  
- Commonly used in APIs and web applications  

In Python, JSON data maps naturally to:
- `dict` → JSON objects  
- `list` → JSON arrays  
- `str`, `int`, `float`, `bool`, `None` → JSON values  

To work with JSON in Python, we use the built-in `json` module.

---

## 🔹 Reading JSON Data

```python
import json

with open("jsonData", "r") as file:
    data = json.load(file)
    print(data)
```

`json.load()`:
- Reads JSON file
- Converts JSON into Python dictionary or list

---

## 🔹 Writing JSON Data

```python
import json

task = [
    {"task": "Buy groceries", "completed": False},
    {"task": "Clean the house", "completed": True},
    {"task": "Pay bills", "completed": False}
]

with open("tasks.json", "w") as file:
    json.dump(task, file, indent=4)
```

`json.dump()`:
- Converts Python object to JSON format
- Writes it into a file  
- `indent=4` makes it readable  

---

## 🔹 Modifying JSON Data

To modify JSON:
1. Load data  
2. Update it  
3. Save it back  

```python
with open("tasks.json", "r") as file:
    tasks = json.load(file)

tasks.append({"task": "Walk the dog", "completed": False})

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)
```

This is the standard JSON update workflow.

---

# 🛠 Project: Mini To-Do App using JSON

We will build a simple persistent CLI application that:
- Adds tasks  
- Displays tasks  
- Updates status  
- Deletes tasks  

---

## Step 1: Setup and File Initialization

```python
import json
import os

TASK_FILE = "my_tasks.json"

if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, "w") as file:
        json.dump([], file)
```

---

## Step 2: Load and Save Functions

```python
def load_tasks():
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=2)
```

---

## Step 3: Add a New Task

```python
def add_task():
    task_name = input("Enter the task name: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task_name, "status": "Incomplete"})
    save_tasks(tasks)
    print(f'Task "{task_name}" added successfully!')
```

---

## Step 4: View All Tasks

```python
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['task']} - {task['status']}")
    else:
        print("No tasks found.")
```

---

## Step 5: Update Task Status

```python
def update_status():
    tasks = load_tasks()
    view_tasks()

    try:
        task_index = int(input("Enter the task number to update: ")) - 1

        if 0 <= task_index < len(tasks):
            new_status = input("Enter the new status (Complete/Incomplete): ").strip()
            tasks[task_index]["status"] = new_status
            save_tasks(tasks)
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a valid task number.")
```

---

## Step 6: Delete a Task

```python
def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_index = int(input("Enter the task number to delete: ")) - 1

        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'Task "{deleted_task["task"]}" deleted successfully!')
        else:
            print("Invalid task number.")

    except ValueError:
        print("Invalid input. Please enter a valid task number.")
```

---

## Step 7: Display Menu

```python
def display_menu():
    print("\n--- Mini To-Do App ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update Task status")
    print("4. Delete a task")
    print("5. Exit")
```

---

## Step 8: Main Program Loop

```python
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
```

---

## 📌 Learning Objectives

- Understand what JSON is  
- Use `json.load()` and `json.dump()`  
- Modify persistent JSON data  
- Handle file initialization safely  
- Build a real-world CLI task manager  
- Implement CRUD operations (Create, Read, Update, Delete)  

---

🚀 Working with JSON is essential for APIs, backend systems, configuration files, and modern application development.