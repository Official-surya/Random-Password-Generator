import string
import random

def generate_password(length, use_letters, use_digits, use_punctuation):
    if length < 10:
        print("Error: Password length must be at least 10 characters.")
        return None

    # Ensuring at least one character from each selected type
    password = []

    if use_letters:
        password.append(random.choice(string.ascii_letters))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_punctuation:
        password.append(random.choice(string.punctuation))

    # Creating the remaining part of the password
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        print("Error: No character types selected. Please select at least one character type.")
        return None

    password += random.choices(characters, k=length - len(password))

    # Shuffling to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Set your parameters here
length = 12  # Desired password length
use_letters = True
use_digits = True
use_punctuation = True

password = generate_password(length, use_letters, use_digits, use_punctuation)

if password:
    print("Generated password:", password)
