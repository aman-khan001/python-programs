# 📚 Python Program to Check Even or Odd

'''
    The even_or_odd function takes a number as input and returns "Even" if the number is even,
    otherwise it returns "Odd". It uses the modulus operator (%) to check for evenness.
    
'''

def even_or_odd(number):
    # Check if the number is even or odd
    return "Even" if number % 2 == 0 else "Odd"

# Example usage
print("Even or Odd:")
print("5 is", even_or_odd(5))  # Output: Odd
print("10 is", even_or_odd(10))  # Output: Even

