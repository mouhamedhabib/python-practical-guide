# 🔹 Dictionaries in Python

This section provides a practical recap of **dictionaries in Python**, including how to create, access, modify, and loop through dictionaries, along with a mini project: a Contact Book.

---

## ❓ What are Dictionaries?

A **dictionary** is a collection which is **unordered, changeable, and indexed**.  

Dictionaries store **key-value pairs** and are written using curly braces `{}`.

Example:

```python
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

contact = {
    'name': 'med',
    'email': 'med@example.com',
    'tel': '1234567890'
}

print(contact)          # Output: {'name': 'med', 'email': 'med@example.com', 'tel': '1234567890'}
print(contact['name'])  # Output: med
```

---

## 🔹 Accessing and Modifying Dictionary Values

You can access values using keys and modify them directly:

```python
print(contact.get('name'))  # Output: med
contact['name'] = 'med habib'
contact['tel'] = '0987654321'
print(contact)
```

---

## 🔹 Adding and Removing Entries

You can add or remove key-value pairs:

```python
contact['address'] = '123 Main St'  # Add new entry
del contact['email']                # Remove entry
print(contact)
```

---

## 🔹 Looping Through a Dictionary

You can iterate through keys and values:

```python
for key in contact:
    print(f"{key}: {contact[key]}")
    if 'email' in contact:
        print(f"Email: {contact['email']}")
    else:
        print("Email not found")
```

---

## 🛠  Project: Contact Book

A simple CLI **Contact Book** to practice dictionaries:

### Features

1. Add a new contact  
2. View all contacts  
3. Search a contact by name  
4. Edit a contact  
5. Delete a contact  
6. Exit  

### Example Code Snippet

```python
# Initialize empty contact book
contacts = {}

# Add a Contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} has been added successfully!")
```

### How it Works

- **Add/Update/Delete** contacts dynamically  
- Stores data in a dictionary: `{name: {"phone": ..., "email": ...}}`  
- Uses loops and conditionals for interactive menu  
- Handles missing entries safely  

---

### ▶️ How to Run

1. Save the script as `contact_book.py`.  
2. Run:

```bash
python contact_book.py
```

---

### 📌 Learning Objectives

- Understand dictionaries in Python  
- Access, modify, add, and remove entries  
- Loop through dictionaries  
- Build a simple interactive CLI application using dictionaries  