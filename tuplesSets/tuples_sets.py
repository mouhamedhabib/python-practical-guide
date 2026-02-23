# Tuples
# syntax: (value1, value2, value3, ...)
myTuple = (1, 2, 3, 'hello', [4, 5], (6, 7))
print(myTuple)

fruit = ('apple', 'banana', 'cherry')
print(fruit[0])  # Output: apple
print(fruit[-1])  # Output: cherry

cordinates = (10, 20,30)
x ,y, z = cordinates
print(cordinates)

# Tuple Operations and Unpacking

vegetables = ('carrot', 'broccoli', 'spinach')
print(len(vegetables))  # Output: 3
print(vegetables + ('tomato', 'cucumber'))  # Output: ('carrot', 'broccoli', 'spinach', 'tomato', 'cucumber')
print(vegetables * 2)  # Output: ('carrot', 'broccoli', 'spinach', 'carrot', 'broccoli', 'spinach')

# Sets
my_set = {1, 2, 3, 'hello', (4, 5)}
print(my_set)
cakes = {'chocolate', 'vanilla', 'strawberry'}
print(cakes)
cakes.add('red velvet')
print(cakes)
cakes.remove('vanilla')
print(cakes)

# Set Operations (Union, Intersection, Difference)
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA.union(setB))  # Output: {1, 2, 3, 4, 5, 6}
print(setA.intersection(setB))  # Output: {3, 4} the some element in setA and setB
print(setA.difference(setB))  # Output: {1, 2}

# Ingredients Checker

# Step 1: Define the recipe ingredients
recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

# Step 2: Get user input for available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

# bonus add to recipe_ingredients 
new_ingredient = input("Enter a new ingredient to add to the recipe: ")
recipe_ingredients.add(new_ingredient)


# Step 3: Compare Ingredients
missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

# Step 4: Display Results
print("\n--- Ingredient Check Results ----")
if missing_ingredients:
    print(
        f"You are missing the following ingredients: {', '.join(missing_ingredients)}"
    )
else:
    print("You have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")
