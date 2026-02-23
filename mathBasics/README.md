# 🔹 Functions in Python

This section provides a practical recap of **functions in Python**, including how to define, call, pass arguments, return values, and a mini project: a Basic Math Quiz Game.

---

## ❓ What are Functions?

A **function** is a block of reusable code that performs a specific task.

- Helps avoid repeating code  
- Makes programs modular and organized  
- Can accept inputs (parameters) and return outputs  

---

## 🔹 Defining and Calling Functions

```python
# Define a simple function
def firstFunction():
    print("This is my first function!")

# Call the function
firstFunction()
```

---

## 🔹 Function Parameters and Arguments

Functions can accept inputs (parameters) and use them in the code:

```python
def user(name):
    print(f"Hello, {name}!")

user("Med")  # Output: Hello, Med!
```

```python
def sumUser(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

sumUser(5, 10)  # Output: The sum of 5 and 10 is 15
```

---

## 🔹 Return Statements

Functions can return a value to be used later:

```python
def sumReturn(a, b):
    return a + b

result = sumReturn(5, 10)
print(result)  # Output: 15
```

---

## 🛠 Project: Basic Math Quiz Game

A simple **Math Quiz Game** using functions:

### Algorithm Overview

1. Ask the user to enter two numbers  
2. Ask the user to choose an operation: `+`, `-`, `*`, `/`  
3. Perform the operation  
4. Display the result  
5. Handle division by zero and invalid operations  

### Example Code

```python
print("\n----- Welcome to the Math Quiz Game! -----\n")

def math_quiz():
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    choice = input("Choose the operation (+, -, *, /): ")

    if choice == '+':
        result = first + second
    elif choice == '-':
        result = first - second
    elif choice == '*':
        result = first * second
    elif choice == '/':
        if second != 0:
            result = first / second
        else:
            print("Error: Division by zero")
            return
    else:
        print("Invalid operation")
        return

    print(f"The result is: {result}")

math_quiz()
```

---

### 📌 Learning Objectives

- Understand and define functions  
- Call functions with or without parameters  
- Use return statements to get values  
- Build a small interactive CLI project using functions  