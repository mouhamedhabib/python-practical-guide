# 🔹 Tuples and Sets in Python

This section provides a practical recap of **tuples and sets in Python**, including how to create, access, modify, perform operations, and a mini project: an Ingredient Checker.

---

## ❓ What are Tuples?

A **tuple** is an **ordered, immutable collection** in Python.  

- Tuples can contain multiple data types  
- Items are indexed starting from 0  
- Tuples cannot be changed after creation  

Example:

```python
myTuple = (1, 2, 3, 'hello', [4, 5], (6, 7))
print(myTuple)

fruit = ('apple', 'banana', 'cherry')
print(fruit[0])  # Output: apple
print(fruit[-1]) # Output: cherry

coordinates = (10, 20, 30)
x, y, z = coordinates  # Tuple unpacking
print(coordinates)
```

---

## 🔹 Tuple Operations and Unpacking

```python
vegetables = ('carrot', 'broccoli', 'spinach')
print(len(vegetables))                     # Output: 3
print(vegetables + ('tomato', 'cucumber')) # Concatenate tuples
print(vegetables * 2)                       # Repeat tuple elements
```

---

## ❓ What are Sets?

A **set** is an **unordered collection of unique items**.  

- Duplicates are not allowed  
- Supports mathematical operations like union, intersection, and difference  

Example:

```python
cakes = {'chocolate', 'vanilla', 'strawberry'}
cakes.add('red velvet')   # Add element
cakes.remove('vanilla')   # Remove element
print(cakes)
```

---

## 🔹 Set Operations

```python
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA.union(setB))        # {1, 2, 3, 4, 5, 6}
print(setA.intersection(setB)) # {3, 4}
print(setA.difference(setB))   # {1, 2}
```

---

## 🛠 Project: Ingredient Checker

A small CLI **Ingredient Checker** to practice sets:

### Steps

1. Define a set of recipe ingredients  
2. Ask user for available ingredients  
3. Allow user to add a new ingredient  
4. Compare user's ingredients with recipe  
5. Display missing and extra ingredients  

### Example Code

```python
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

new_ingredient = input("Enter a new ingredient to add to the recipe: ")
recipe_ingredients.add(new_ingredient)

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("\n--- Ingredient Check Results ----")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")
```

---

### 📌 Learning Objectives

- Understand **tuples** and their immutability  
- Perform tuple operations and unpacking  
- Understand **sets** and uniqueness  
- Use set operations: union, intersection, difference  
- Build a small interactive CLI project using sets  