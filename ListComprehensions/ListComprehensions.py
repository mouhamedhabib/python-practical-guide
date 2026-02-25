# List Comprehensions
# List comprehensions are a concise way to create lists in Python. They consist of brackets containing an expression followed by a for clause, and optionally, one or more if clauses.
# Basic Syntax:


squares = [x**2 for x in range(10)]
print(squares)
# This will create a list of squares for numbers from 0 to 9.
# x here is the variable that takes the value of each item in the iterable (in this case, range(10)) and x**2 is the expression that is evaluated and added to the list for each item.

# Basic Syntax and Examples

number = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in number]
print(doubled)
# Output: [2, 4, 6, 8, 10]
# start with a list of numbers 1 *2 , 2*2, 3*2, 4*2, 5*2

# Filtering with List Comprehensions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, 8, 10]
# This creates a list of even numbers from the original list by including an if condition that checks if the number is divisible by 2.
names = ["John", "Jane", "Doe", "Smith" ,"medHabibccc"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# Using Conditional Statements

num = [1, 2, 3, 4, 5]
labels = ["odd" if x % 2 != 0 else "even" for x in num]
print(labels)
# Output: ['odd', 'even', 'odd', 'even', 'odd']

# Student Grade Manager

# Step 1: Get student scores
student_scores = input("Enter student scores separated by commas: ")
scores = [int(score) for score in student_scores.split(",")]

# Step 2: Assign Grades using List Comprehension
grades = [
    (
        "A"
        if score >= 90
        else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    )
    for score in scores
]

# Step 3: Filter Passing and Failing Students
passing_students = [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]

# Step 4: Print Results
print("\n--- Student Grades ----")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n--- Passing and Failing Students ---")
print("Passing Students:", passing_students)
print("Failing Students:", failing_students)
