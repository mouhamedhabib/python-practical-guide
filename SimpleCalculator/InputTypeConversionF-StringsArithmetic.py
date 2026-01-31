# Ask the user to enter their name
from typing import Literal


user = input("Enter your name ")

# Print a welcome message using f-string
print(f"Hello {user}")


# ===============================
# Type Conversion (int and float)
# ===============================

# Ask the user to enter a number and convert it to integer
num = int(input("Enter a number "))

# Multiply the number by 2 and print the result
print(f"num * 2 = {num * 2}")


# Ask the user to enter a number and convert it to float
num1 = float(input("Enter a number "))

# Multiply the float number by 2
print(f"num1 * 2 = {num1 * 2}")


# Ask the user to enter a value as string
num2 = str(input("Enter a number "))

# Multiply string by 2 (this repeats the string)
print(f"num2 * 2 = {num2 * 2}")


# ===============================
# String Formatting with f-Strings
# ===============================

# Ask the user for two numbers
num3 = int(input("Enter a number num3 "))
num4 = int(input("Enter a number num4 "))

# Add the two numbers
result = num3 + num4

# Print the result using f-string
print(f"num3: {num3} + num4: {num4} = {result}")


# ===============================
# Basic Arithmetic Operations
# ===============================

a = 10
b = 5

# Print different math operations
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")


# ===============================
# Project: Simple Calculator
# ===============================

# Ask the user for two numbers
num5 = float(input("Enter first input: "))
num6 = float(input("Enter second input: "))
choix = input("Enter your operation (+, -, *, /, //): ")

if choix == "+":
    result = num5 + num6

elif choix == "-":
    result = num5 - num6

elif choix == "*":
    result = num5 * num6

elif choix == "/":
    if num6 != 0:
        result = num5 / num6
    else:
        print("Cannot divide by zero")
        exit()

elif choix == "//":
    if num6 != 0:
        result = num5 // num6
    else:
        print("Cannot divide by zero")
        exit()

else:
    print("Invalid operation")
    exit()

print(f"{num5} {choix} {num6} = {result}")


# Avoid division by zero
# modules: float | Literal['Cannot divide by zero'] = num5 % num6 if num6 != 0 else "Cannot divide by zero"


# exponentiation = num5**num6

# # Print all results
# print(f"Addition: {plus}")
# print(f"Subtraction: {subtraction}")
# print(f"Division: {division}")
# print(f"Floor Division: {floor_division}")
# print(f"Multiplication: {multiplication}")
# print(f"Modulus: {modules}")
# print(f"Exponentiation: {exponentiation}")
