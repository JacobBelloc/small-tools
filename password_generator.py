import random
import string

def generate_password(length=8):
    # Generate a random password consisting of letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
