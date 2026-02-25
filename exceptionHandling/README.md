# 🔹 Exceptions Handling in Python

This section explains what exceptions are, how to handle them using `try`, `except`, `else`, and `finally`, how to raise custom exceptions, and includes a practical project: **Safe Calculator**.

---

## ❓ What are Exceptions?

An **exception** is an error that occurs during program execution.

Common examples:
- `ZeroDivisionError` → dividing by zero
- `ValueError` → invalid type conversion
- `TypeError` → wrong data type operation

Basic example:

```python
try:
    num1 = int(input("Enter a number: "))
    result = 10 / num1
    print("The result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
```

---

## 🔹 Using try, except, else, and finally

Structure:

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Runs if no exception occurs
finally:
    # Always runs
```

Example:

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result is:", result)
finally:
    print("This will always execute.")
```

📌 Key Logic:
- `try` → risky code  
- `except` → handle errors  
- `else` → runs only if no error  
- `finally` → always executes  

---

## 🔹 Handling Multiple Exceptions

You can catch multiple exceptions in one block:

```python
try:
    num2 = int(input("Enter another number: "))
    result2 = 10 / num2
except (ZeroDivisionError, ValueError) as e:
    print("An error occurred:", e)
```

This keeps the code clean and readable.

---

## 🔹 Raising Custom Exceptions

You can manually raise exceptions using `raise`.

Example:

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    print("Withdraw successful:", amount)

try:
    withdraw(10)
except ValueError as e:
    print("Error:", e)
```

📌 Why raise exceptions?
- Enforce business rules
- Prevent invalid logic
- Make debugging easier

---

# 🛠 Project: Safe Calculator

We will build a calculator that safely handles:
- Invalid inputs
- Division by zero
- Unexpected errors

---

## Step 1: Define Calculator Functions

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
```

---

## Step 2: Display Menu

```python
def show_menu():
    print("\n--- Safe Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
```

---

## Step 3: Main Program

```python
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Safe Calculator!... Restarting...")
```

---

## 📌 Learning Objectives

- Understand what exceptions are  
- Use `try`, `except`, `else`, and `finally` correctly  
- Handle multiple exceptions cleanly  
- Raise custom exceptions  
- Build a safe CLI application  
- Write production-style defensive code  

---

🚀 Exception handling is critical for writing stable, professional, and production-ready Python applications.