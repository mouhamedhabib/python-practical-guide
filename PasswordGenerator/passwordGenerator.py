# Modules and Libraries
import math
print(math.sqrt(16))
print(math.pi)

import random
print(random.randint(1, 100))

from random import choice
colors = ["red", "green", "blue", "yellow"]
print(choice(colors))

from random import * # This imports all functions from the random module, allowing you to use them directly without the random. but is consumed more memory and can lead to conflicts if there are functions with the same name in different modules.
print(randint(1, 100))

# Built-in Python Libraries
from random import choice
password = ''.join(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()') for _ in range(8))
print("Generated Password:", password)

# Random Password Generator
import random, string

# Step 1: Define Password Generation Function


def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Character sets for the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Ensure at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the remaining length with random choices from all sets
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string and return
    return "".join(password)


# STep 2: User Interaction

try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(e)
