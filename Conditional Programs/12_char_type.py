# 📚 Python Program to Determine Character Type
# This program defines a function to determine the type of a character (uppercase, lowercase, digit, or special character).

'''
    The char_type function takes a character as input and returns a string describing its type.
    It checks if the character is uppercase, lowercase, a digit, or a special character.
'''

def char_type(char):
    """
    Determines the type of a character (uppercase, lowercase, digit, or special character).
    
    Args:
        char (str): The character to check.
        
    Returns:
        str: A string describing the type of the character.
    """
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special Character"
    
# Example usage
print("Character Type:")
print("A is", char_type('A'))      # Output: Uppercase
print("a is", char_type('a'))      # Output: Lowercase
print("5 is", char_type('5'))      # Output: Digit
print("@ is", char_type('@'))      # Output: Special Character