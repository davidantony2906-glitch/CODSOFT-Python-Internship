import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"

    all_characters = lowercase + uppercase + digits + special_chars
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Password length should be at least 4.")
    else:
        result = generate_password(length)
        print("Generated Password:", result)

except ValueError:
    print("Please enter a valid number.")