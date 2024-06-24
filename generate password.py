import random
import string

def generate_password(length):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Ask the user for the password length
password_length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(password_length)
print("Generated password:", password)
