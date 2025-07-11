# 📚 Python Program to Determine Number Type
# This program defines a function to determine if a number is even, odd, positive, negative, or zero.

'''
    The number_type function takes an integer as input and returns a string describing its type.
    It checks if the number is zero, positive or negative, and whether it is even or odd.
'''


def number_type(num):
    """
    Determines the type of a number (even, odd, positive, negative, or zero).
    
    Args:
        num (int): The number to check.
    
    Returns:
        str: A string describing the type of the number.
    """
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive " + ("Even" if num % 2 == 0 else "Odd")
    else:
        return "Negative " + ("Even" if num % 2 == 0 else "Odd")
# Example usage
print("Number Type:")
print("5 is", number_type(5))    # Output: Positive Odd
print("10 is", number_type(10))  # Output: Positive Even
print("-3 is", number_type(-3))  # Output: Negative Odd
print("-8 is", number_type(-8))  # Output: Negative Even