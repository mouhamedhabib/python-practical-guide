# What is File Writing in Python?
# python provides built-in functions and methods to write data to files. The most common way to write to a file is by using the `open()` function with the appropriate mode (e.g., 'w' for writing, 'a' for appending). When you open a file in write mode, it will create the file if it does not exist or overwrite the file if it already exists.

# Writing to Files (w mode)
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n") 

# Appending to Files (a mode)
with open("example.txt", "a") as file:
    file.write("This line will be appended to the file.\n")

# Handling File Writing Errors
try:
    with open("/invalid_path/example.txt", "w") as file:
        file.write("This will raise an error.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}") 

# Daily Journal Logger

# Step 1: Define the journal file
JOURNAL_FILE = "daily_journal.txt"


# Step 2: Add a new entry
def add_entry():
    entry = input("Write your journal entry: ")
    with open(JOURNAL_FILE, "a") as file:
        file.write(entry + "\n")
    print("Entry added successfully!")


# Step 3: View all entries
def view_entries():
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Journal Entries ---")
                print(content)
            else:
                print("No entries found. Start writing today")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")


# Step 4: Search entries by keyword
def search_entries():
    keyword = input("Enter a keyword to search for: ").lower()
    try:
        with open(JOURNAL_FILE, "r") as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results ---")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")


# Step 5: Display Menu
def show_menu():
    print("\n--- Daily Journal Logger ---")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Exit")


# Step 6: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
