import string
import secrets
def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
