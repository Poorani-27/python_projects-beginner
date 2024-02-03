import random
import string 
def generate_password(length):
    characters = string.ascii_letters + string.ascii_lowercase +string.ascii_uppercase +string.punctuation +string.hexdigits +string.digits 
    password =''.join(random.choice(characters) for _ in range(length))
    return password
print("\nEnter the length of the password")
password_length = int(input())
New_password = generate_password(password_length)
print(New_password)