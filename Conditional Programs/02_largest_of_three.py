# 📚 Python Program to Find the Largest of Three Integers
# This program defines a function to find the largest of three integers.

'''
    The largest_of_three function takes three integers as input
    and returns the largest integer among them.
    It uses conditional statements to compare the integers.
'''

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
# Example usage
print("Largest of 3, 5, and 2:", largest_of_three(3, 5, 2))  # Output: 5
print("Largest of 10, 20, and 15:", largest_of_three(10, 20, 15))  # Output: 20
