import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits  
    password = ''.join(random.choices(characters, k=8)) 
    return password

print("Generated Password:", generate_password())