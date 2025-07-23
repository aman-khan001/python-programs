# 📚 Python Program to Check Triangle Validity


'''
    The is_valid_triangle function takes three sides of a triangle as inputs
    and returns True if they can form a valid triangle, otherwise returns False.
    A triangle is valid if the sum of any two sides is greater than the third side.
'''

def is_valid_triangle(a, b, c):
    """
    Check if three sides can form a valid triangle.
    A triangle is valid if the sum of any two sides is greater than the third side.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)  

# Example usage
print("Triangle Validity Check:")
print("Sides 3, 4, 5:", is_valid_triangle(3, 4, 5))  # Output: True
print("Sides 1, 2, 3:", is_valid_triangle(1, 2, 3))  # Output: False
