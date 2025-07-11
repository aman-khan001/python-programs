# 📘 Program: Find Square Root of a Number
# This program defines a function to calculate the square root of a number.

'''
    The square_root function takes a number as input and returns its square root.
    It uses the exponentiation operator (**) to compute the square root.
'''

def square_root(num):
    '''if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    elif num == 0:
        return 0
    elif num == 1:
        return 1'''
    return num ** 0.5

# Example usage

print("Square root of 25:", square_root(25))  # Output: 5.0
print("Square root of 100:", square_root(100))  # Output: 10.0
print("Square root of 16:", square_root(16))  # Output: 4.0
print("Square root of 2:", square_root(2))    # Output: 1.4142135623730951

# 🧠 Explanation:
# The square_root function computes the square root of a number using the exponentiation operator.
# Power 0.5 is equivalent to taking the square root.