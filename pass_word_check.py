password = input("Enter your password: ")
is_long_enough = len(password) >= 10
has_uppercase = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special_char = any(not char.isalnum() for char in password)
'''Evaluate password strength based on criteria'''
if is_long_enough and has_uppercase and has_digit and has_special_char:
    print("it's a Strong password")
elif is_long_enough and (has_uppercase or has_digit or has_special_char):
    missing_criteria = []
    if not has_uppercase:
        missing_criteria.append("an uppercase letter")
    if not has_digit:
        missing_criteria.append("a digit")
    if not has_special_char:
        missing_criteria.append("a special character")
    print("it's a Medium password")
    print("Missing:", ", ".join(missing_criteria))
    print("Special Character is:", sum(not char.isalnum() for char in password), "special character")
    print("Digit is:", sum(char.isdigit() for char in password), "digit")
    print("Uppercase Letter is:", sum(char.isupper() for char in password), "uppercase letter")
else:
    print("it's a Weak password")
    print("Special Character is:", sum(not char.isalnum() for char in password), "special character")
    print("Digit is:", sum(char.isdigit() for char in password), "digit")
    print("Uppercase Letter is:", sum(char.isupper() for char in password), "uppercase letter")