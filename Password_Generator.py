import random
import string

def generate_password(length, include_uppercase=True, include_special_chars=True, include_numbers=True):

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_special_chars:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"

password = generate_password(length, include_uppercase, include_special_chars, include_numbers)
print("Generated Password:", password)
