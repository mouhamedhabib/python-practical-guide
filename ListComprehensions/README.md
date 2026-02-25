# 🔹 List Comprehensions in Python

This section explains what **List Comprehensions** are, how to use them with filtering and conditional logic, and includes a practical project: **Student Grade Manager**.

---

## ❓ What are List Comprehensions?

A **List Comprehension** is a concise way to create lists in Python.

### Basic Structure:

```python
[expression for item in iterable]
```

Optional filtering:

```python
[expression for item in iterable if condition]
```

They make code:
- Cleaner
- More readable
- More Pythonic
- Faster than traditional loops (in many cases)

---

## 🔹 Basic Syntax and Examples

### Example 1: Squares of Numbers

```python
squares = [x**2 for x in range(10)]
print(squares)
```

Output:

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Explanation:
- `x` takes each value from `range(10)`
- `x**2` is evaluated and added to the list

---

### Example 2: Doubling Numbers

```python
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)
```

Output:

```
[2, 4, 6, 8, 10]
```

---

## 🔹 Filtering with List Comprehensions

You can filter elements using an `if` condition.

### Example: Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
```

Output:

```
[2, 4, 6, 8, 10]
```

---

### Example: Filter Short Names

```python
names = ["John", "Jane", "Doe", "Smith", "medHabibccc"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)
```

---

## 🔹 Using Conditional Statements (Inline If-Else)

You can use inline conditions inside list comprehensions.

### Example:

```python
num = [1, 2, 3, 4, 5]
labels = ["odd" if x % 2 != 0 else "even" for x in num]
print(labels)
```

Output:

```
['odd', 'even', 'odd', 'even', 'odd']
```

Structure:

```python
[true_value if condition else false_value for item in iterable]
```

---

# 🛠 Project: Student Grade Manager

We will use list comprehensions to:
- Convert input into integers
- Assign grades
- Filter passing and failing students

---

## Step 1: Get Student Scores

```python
student_scores = input("Enter student scores separated by commas: ")
scores = [int(score) for score in student_scores.split(",")]
```

---

## Step 2: Assign Grades

```python
grades = [
    (
        "A"
        if score >= 90
        else "B"
        if score >= 80
        else "C"
        if score >= 70
        else "D"
        if score >= 60
        else "F"
    )
    for score in scores
]
```

---

## Step 3: Filter Passing and Failing Students

```python
passing_students = [score for score in scores if score >= 60]
failing_students = [score for score in scores if score < 60]
```

---

## Step 4: Display Results

```python
print("\n--- Student Grades ----")
for i, (score, grade) in enumerate(zip(scores, grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n--- Passing and Failing Students ---")
print("Passing Students:", passing_students)
print("Failing Students:", failing_students)
```

---

## 📌 Learning Objectives

- Understand list comprehension syntax  
- Replace loops with concise expressions  
- Apply filtering conditions  
- Use inline conditional expressions  
- Build a small grading system  
- Write clean, professional Python code  

---

🚀 List comprehensions are a core Python skill — mastering them makes your code cleaner, faster, and more advanced.