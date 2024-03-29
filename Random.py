import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage: generate a random password of length 12
random_password = generate_random_password()
print("Random Password:", random_password)