# Functions
# 1 create a function that takes two numbers as parameters and returns their sum.
# 2 call the function

# 1 create a function
def firstFunction():
    # code block in side function
    print("This is my first function!")
# 2 call the function
firstFunction()

# Function Parameters and Arguments
def user(name):
    print(f"Hello, {name}!")
user("Med")

def sumUser(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
sumUser('med' , " habib")


def sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

sum(5, 10)

# Return Statements
def sumReturn(a, b):
    return a + b
result = sumReturn(5, 10)
print(result)

# Project: Basic Math Quiz Game

# Algorithm Math_Quiz
# Variables
#     first, second : Integer
#     choice        : Character
#     result        : Real

# Begin
#     Write "----- Welcome to the Math Quiz Game! -----"

#     Write "Enter the first number:"
#     Read first

#     Write "Enter the second number:"
#     Read second

#     Write "Choose the operation (+, -, *, /):"
#     Read choice

#     If choice = '+' Then
#         result ← first + second
#     Else If choice = '-' Then
#         result ← first - second
#     Else If choice = '*' Then
#         result ← first * second
#     Else If choice = '/' Then
#         If second ≠ 0 Then
#             result ← first / second
#         Else
#             Write "Error: Division by zero"
#             Stop
#         End If
#     Else
#         Write "Invalid operation"
#         Stop
#     End If

#     Write "The result is:", result
# End


print('/n ----- Welcome to the Math Quiz Game! ----- /n')
def math_quiz():
    frist = int(input(" create frist number: "))
    second = int(input(" create second number: "))
    choise = input(" choose the operation (+, -, *, /): ")
    if choise == '+':
        result = frist + second
    elif choise == '-':
        result = frist - second
    elif choise == '*':
        result = frist * second
    elif choise == '/':
        result = frist / second
    else:
        print("Invalid operation")
        return
    print(f"The result is: {result}")
math_quiz()
