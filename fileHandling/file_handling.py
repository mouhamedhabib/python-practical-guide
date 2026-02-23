# File Handling
# file handling is the process of creating, reading, updating, and deleting files on a computer. In Python, you can use the built-in `open()` function to work with files.

# file = open('filename.txt', 'mode')
# The `mode` parameter specifies the mode in which the file is opened. The most common
# r = for reading (default)
# w = for writing (creates a new file or overwrites an existing file)
# a = for appending (adds content to an existing file or creates a new file)
# b = for binary mode (used for non-text files like images or PDFs)
# file = open('example.txt', 'r')  # Open a file for reading

with open('filename.txt', 'r') as file:  # Using 'with' statement to ensure proper file handling
    content = file.read()  # Read the entire content of the file
    print(content)

# adding content to a file
with open('filename.txt', 'a') as file:  # Open a file for writing
    file.write("Hello, this is a new file created using Python.\n")  # Write a line to the file
    file.write("hello world.\n")  # Write another line to the file

# writing to a file (overwriting existing content)
with open('filename.txt', 'w') as file:  # Open a file for writing
    file.write("This content will overwrite the existing content in the file.\n")  # Write a line to the file
    file.write("This is another line that will overwrite the previous content.\n")  # Write another line to the file

# Note-Taking App
# Step 1: Define file name
FILE_NAME = "myNotes.txt"


# Step 2: Display menu options
def show_menu():
    print("\n--- Note-Taking App Menu ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")


# Step 3: Add a new note
def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")


# Step 4: View all notes
def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n--- Your Notes ---")
                print(content)
            else:
                print("\nNo notes found.")
    except FileNotFoundError:
        print("No notes found.")


# Step 5: Delete all notes
def delete_notes():
    confirm = input("Are you sure you want to delete all notes? (Yes/n): ")
    if confirm.lower() == "yes":
        with open(FILE_NAME, "w") as file:
            pass
        print("All notes have been deleted")
    else:
        print("Deletion cancelled")


# Step 6: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Exiting Note-Taking App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
