# 🔹 File Reading in Python

This section explains how file reading works in Python, different reading modes, error handling, and includes a practical project: **Recipe Viewer App**.

---

## ❓ What is File Reading in Python?

File reading in Python means:
1. Opening a file  
2. Reading its contents  
3. Closing the file  

Python provides built-in tools through the `open()` function.

The recommended way to work with files is using the `with` statement because it:
- Automatically closes the file
- Prevents resource leaks
- Handles exceptions safely

---

## 🔹 Reading Files Using `open()`

### Example 1: Read Entire File

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### Example 2: Read Line by Line

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Using `.strip()` removes extra whitespace and newline characters.

---

## 🔹 Reading Modes (`r`, `rb`, `r+`)

| Mode | Description |
|------|------------|
| `"r"`  | Read mode (default). Raises `FileNotFoundError` if file does not exist |
| `"rb"` | Read binary mode (used for images, PDFs, etc.) |
| `"r+"` | Read and write mode |

---

### Example: Binary Mode

```python
try:
    with open("example.txt", "rb") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
```

---

## 🔹 Handling File Reading Errors

Always handle possible exceptions:

```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
```

This makes your application more stable and production-ready.

---

# 🛠 Project: Recipe Viewer App

We will build a simple CLI application that:
- Loads recipes from a file
- Displays recipe details
- Lists all available recipes

---

## Step 1: Load Recipes from File

```python
def load_recipes(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}

            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace("Ingredients: ", "").strip()
                    instructions = lines[2].replace("Instructions: ", "").strip()

                    recipe_dict[name] = {
                        "ingredients": ingredients,
                        "instructions": instructions,
                    }

            return recipe_dict

    except FileNotFoundError:
        print("File not found.")
        return {}
```

---

## Step 2: Display Menu

```python
def show_menu():
    print("\n--- Recipe Viewer Menu ---")
    print("1. View Recipe by Name")
    print("2. List All Recipes")
    print("3. Exit")
```

---

## Step 3: View Recipe Details

```python
def view_recipe(recipes):
    name = input("Enter the name of the recipe: ").strip()

    if name in recipes:
        print(f"\n--- Recipe {name} Details ---")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print("Recipe not found.")
```

---

## Step 4: Main Program

```python
recipe_file = "recipes.txt"
recipes = load_recipes(recipe_file)

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        view_recipe(recipes)
    elif choice == "2":
        print("\n--- All Recipes ---")
        for name in recipes:
            print(name)
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
```

---

## 📌 Learning Objectives

- Understand how file reading works  
- Use different file modes (`r`, `rb`, `r+`)  
- Read full files and line-by-line  
- Handle file-related exceptions  
- Build a real CLI file-based application  
- Work with structured text data  

---

🚀 File reading + file writing together = foundation for building real-world Python applications like log systems, data processors, and mini-databases.