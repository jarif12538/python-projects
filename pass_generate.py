import string
import secrets
def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    guranteed_characters = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]
    store = lowercase + uppercase + digits + special
    password = guranteed_characters + [secrets.choice(store) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
print(generate_password(20))