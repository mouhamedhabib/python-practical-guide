# 🔹 If-Else Statements, Comparison Operators & Nested If-Else in Python

This section provides a practical recap of **conditional statements in Python**, including if-else statements, comparison operators, logical operators, and nested conditions.

---

## ❓ What are If-Else Statements?

**If-Else statements** allow you to execute different blocks of code depending on whether a condition is True or False.

Example:

```python
num = 10

if num > 5:
    print("num is greater than 5")
elif num == 5:
    print("num is equal to 5")
else:
    print("num is less than 5")
```

- `if` checks a condition  
- `elif` checks another condition if the previous `if` was False  
- `else` runs if all previous conditions are False  

---

## 🔹 Comparison Operators

Comparison operators are used to compare values:

| Operator | Meaning          | Example       |
|----------|-----------------|---------------|
| `>`      | Greater than     | `5 > 3` → True |
| `<`      | Less than        | `2 < 4` → True |
| `==`     | Equal to         | `5 == 5` → True |
| `!=`     | Not equal to     | `5 != 3` → True |
| `>=`     | Greater or equal | `5 >= 5` → True |
| `<=`     | Less or equal    | `3 <= 5` → True |

---

## 🔹 Logical Operators

Logical operators combine multiple conditions:

| Operator | Meaning | Example |
|----------|---------|---------|
| `and`    | True if both conditions are True | `x > 5 and y > 5` |
| `or`     | True if at least one condition is True | `x > 5 or y > 5` |
| `not`    | Negates the condition | `not(x > 5)` |

Example:

```python
x = 5
y = 10

if x > 5 and y > 5:
    print("both conditions are true")
else:
    print("the condition here is False")
```

---

## 🔹 Nested If-Else Statements

Nested if-else statements are **if statements inside another if or else block**, used for more complex decision-making.

Example:

```python
user = float(input("Enter a number "))
user1 = float(input("Enter a number "))

if user > user1:
    print(f"{user} is greater than {user1}")
elif user == user1:
    print(f"{user} is equal to {user1}")
else:
    print(f"{user} is less than {user1}")

if user == 0 and user1 == 0:
    print('both numbers are zero')
else:
    print('one number is not zero')
```

---

## 🛠 Project: Number Comparison Tool

A small CLI project that allows the user to:

- Compare two numbers  
- Check equality  
- Detect if both numbers are zero  
- Print results clearly in the console  

**Learning Objectives:**

- Understand and use if-else statements  
- Apply comparison operators (`>`, `<`, `==`)  
- Combine conditions with logical operators (`and`, `or`)  
- Build nested conditions for more advanced logic  
- Create a small interactive Python CLI tool  