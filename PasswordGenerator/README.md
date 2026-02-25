# 🔹 Modules and Libraries in Python

This section explains how Python modules and libraries work, how to import them, and includes a practical project: **Random Password Generator**.

---

## ❓ What are Modules and Libraries?

- A **Module** is a Python file containing functions, variables, or classes that you can reuse.
- A **Library** is a collection of related modules.
- Python provides many **built-in libraries** such as `math`, `random`, and `string`.

Using modules helps:
- Reuse code
- Avoid rewriting common logic
- Keep projects organized
- Improve scalability

---

## 🔹 Importing Modules

There are different ways to import modules:

### 1️⃣ Import the whole module

```python
import math
print(math.sqrt(16))
print(math.pi)
```

```python
import random
print(random.randint(1, 100))
```

---

### 2️⃣ Import specific functions

```python
from random import choice

colors = ["red", "green", "blue", "yellow"]
print(choice(colors))
```

---

### 3️⃣ Import everything (Not Recommended in Real Projects)

```python
from random import *
print(randint(1, 100))
```

⚠️ This approach:
- Uses more memory
- Can create name conflicts
- Reduces code clarity

Use it carefully in professional projects.

---

## 🔹 Built-in Python Libraries Example

```python
from random import choice

password = ''.join(
    choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()')
    for _ in range(8)
)

print("Generated Password:", password)
```

---

## 🛠 Project: Random Password Generator

We will build a secure password generator using:
- `random`
- `string`

---

### Step 1: Define Password Generation Function

```python
import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return "".join(password)
```

---

### Step 2: User Interaction

```python
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(e)
```

---

## 🔹 Creating and Using Custom Modules

You can create your own module:

### Example: mymodule.py

```python
def greet(name):
    return f"Hello, {name}!"
```

### Use it in another file:

```python
import mymodule
print(mymodule.greet("Ali"))
```

---

## 📌 Learning Objectives

- Understand what modules and libraries are  
- Learn different ways to import modules  
- Use built-in libraries (`math`, `random`, `string`)  
- Understand why `from module import *` is risky  
- Build a practical **Random Password Generator**  
- Create and use custom modules  

---

🚀 Now you understand how Python modularity works — and this is a core skill for building scalable, professional applications.