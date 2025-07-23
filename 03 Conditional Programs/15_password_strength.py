# 📚 Python Program to Check Password Strength

"""
  This program checks the strength of a password based on certain criteria.
  The password must:
    1. Be at least 6 characters long.
    2. Contain at least one uppercase letter.
    3. Contain at least one lowercase letter.
    4. Contain at least one digit.
    5. Contain at least one special character.
    6. Be at least 8 characters long for a strong password.
"""

def password_strength(password = ""):
    #  Check if the password is empty
    if len(password) < 6:
        return "Weak: Password must be at least 6 characters long."
    #  Check for uppercase, lowercase, digit, and special character
    elif not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    #  Check for lowercase, digit, and special character
    elif not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    #  Check for digit and special character
    elif not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    #  Check for special character
    elif not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        return "Weak: Password must contain at least one special character."
    #  Check for length for medium and strong passwords
    elif len(password) < 8:
        return "Medium: Password is acceptable but could be stronger."
    else:
        return "Strong: Password is strong."
    
# Example usage
print("Password Strength Check:")
print("Password 'abc':", password_strength("abc"))  # Output: Weak
print("Password 'Abc123':", password_strength("Abc123"))  # Output: Weak
print("Password 'Abc123!':", password_strength("Abc123!"))  # Output: Strong
