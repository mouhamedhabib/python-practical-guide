# 🔹 Lists in Python

This section provides a practical recap of **lists in Python**, including how to create, access, modify, and loop through lists, along with a mini project: a Shopping List App.

---

## ❓ What are Lists?

A **list** is an **ordered, changeable collection** of items in Python.  

- Lists allow duplicate values  
- Items are indexed starting from 0  
- Lists can hold any data type  

Example:

```python
shopping_list = ["Milk", "Eggs", "Bread"]
print(shopping_list[1])  # Output: Eggs
```

---

## 🔹 List Operations

You can **add, remove, or access items** in a list:

```python
shopping_list.append("Butter")   # Add item at the end
shopping_list.insert(1, "Juice") # Insert item at index 1
print(shopping_list)
```

```python
shopping_list.remove("Bread")     # Remove an item
popped_item = shopping_list.pop(0)  # Remove first item
shopping_list.clear()             # Remove all items
```

---

## 🔹 Looping Through Lists

```python
for item in shopping_list:
    print(f"- {item}")

for index, item in enumerate(shopping_list):
    print(f"{index + 1}. {item}")
```

---

## 🔹 List Methods

- `append()` – add an item at the end  
- `insert()` – add an item at a specific position  
- `remove()` – remove an item by value  
- `pop()` – remove an item by index  
- `clear()` – remove all items  
- `sort()` – sort the list  
- `reverse()` – reverse the list  

---

## 🛠 Project: Shopping List App

A simple **CLI Shopping List App** to practice list operations.

### Features

1. View the shopping list  
2. Add an item  
3. Remove an item  
4. Clear the entire list  
5. Exit  

### Example Code

```python
shopping_list = []

def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear List")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n--- Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")

    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")

    elif choice == "4":
        shopping_list.clear()
        print("The shopping list has been cleared.")

    elif choice == "5":
        print("Goodbye! Happy Shopping!")
        break

    else:
        print("Invalid choice. Please try again.")
```

---

### 📌 Learning Objectives

- Understand Python lists  
- Perform common list operations: add, remove, access items  
- Loop through lists using `for` loops  
- Use built-in list methods (`append`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`)  
- Build a small interactive CLI project using lists  