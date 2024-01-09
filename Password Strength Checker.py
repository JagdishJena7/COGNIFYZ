import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long"
    
    # Check for the presence of uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Weak: Password should contain both uppercase and lowercase letters"
    
    # Check for the presence of digits
    if not any(c.isdigit() for c in password):
        return "Weak: Password should contain at least one digit"
    
    # Check for the presence of special characters (symbols)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character"
    
    return "Strong: Password meets all criteria"

# Get user input
user_password = input("Enter a password: ")

# Check password strength and print the result
result = check_password_strength(user_password)
print(result)
