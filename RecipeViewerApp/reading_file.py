#  What is File Reading in Python?
# File reading in Python refers to the process of opening a file, reading its contents, and then closing the file. This is typically done using built-in functions and methods provided by Python's standard library. The most common way to read a file is by using the `open()` function, which returns a file object that can be used to read the contents of the file.

# Reading Files Using open()
# To read a file in Python, you can use the `open()` function along with the `read()` method. Here's a simple example:

# with guarantee that the file will be properly closed after its suite finishes, even if an exception is raised on the way. The `with` statement is used to wrap the execution of a block with methods defined by a context manager.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading Modes (r, rb, r+)
# r - Read mode: This is the default mode. It allows you to read the contents of a file. If the file does not exist, it will raise a FileNotFoundError.
# rb - Read binary mode: This mode is used for reading binary files, such as images or PDFs. It reads the file as bytes rather than text.
# r+ - Read and write mode: This mode allows you to read and write to the same file. If the file does not exist, it will raise a FileNotFoundError.
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.") 

try:
    with open("example.txt", "rb") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

# Recipe Viewer App


# Step 1: Load Recipes from File
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


# Step 2: Display Recipe Menu
def show_menu():
    print("\n--- Recipe Viewer Menu ---")
    print("1. View Recipe by Name")
    print("2. List All Recipes")
    print("3. Exit")


# Step 3: Display Recipe Details
def view_recipe(recipes):
    name = input("Enter the name of the recipe: ").strip()
    if name in recipes:
        print(f"\n--- Recipe {name} Details ---")
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print("Recipe not found.")


# Step 4: Main Program
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
