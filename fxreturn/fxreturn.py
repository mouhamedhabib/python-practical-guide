# Understanding Return Values in Functions
def addNumbers(a, b):
    return a + b
    resultat = addNumbers(5, 3)
resultat = addNumbers(5, 3)
print(resultat)  # Output: 8

# Using Functions to Perform Calculations

def rectangleArea(length, width):
  return length * width
area = rectangleArea(5, 3)
print(area)  # Output: 15

# How to Return Multiple Values
def mathOperations(x, y):
    sum_result = x + y
    diff_result = x - y
    prod_result = x * y
    return sum_result, diff_result, prod_result
result = mathOperations(10, 5)
print(result)  # Output: (15, 5, 50)

