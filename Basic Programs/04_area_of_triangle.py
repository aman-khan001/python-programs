# 📚 Python Program to Calculate the Area of a Triangle
# This program defines a function to calculate the area of a triangle.

'''
    The area_of_triangle function takes the base and height of a triangle as inputs
    and returns the area using the formula: Area = 0.5 * base * height.
'''

def area_of_triangle(base, height):
    """
    Calculate the area of a triangle given its base and height.
    Formula = (1/2) × base × height
    """
    return 0.5 * base * height

# Example usage
print("Area of triangle with base 10 and height 5:", area_of_triangle(10, 5))  # Output: 25.0
print("Area of triangle with base 7 and height 3:", area_of_triangle(7, 3))    # Output: 10.5
