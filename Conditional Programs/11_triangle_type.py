# 📚 Python Program to Determine Triangle Type

'''
    The triangle_type function takes three side lengths as inputs
    and returns the type of triangle:
    - Equilateral: All sides are equal
    - Isosceles: Two sides are equal
    - Scalene: All sides are different
    - Not a triangle: If any side length is less than or equal to zero or if the triangle inequality is not satisfied
'''

def triangle_type(a, b, c):
    """
    Determine the type of triangle based on the lengths of its sides.
    
    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c
    
    Returns:
    str: Type of triangle ('Equilateral', 'Isosceles', 'Scalene', 'Not a triangle')
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"
    
# Example usage
print("Triangle Type:")
print("Sides 3, 3, 3:", triangle_type(3, 3, 3))  # Output: Equilateral
print("Sides 5, 5, 8:", triangle_type(5, 5, 8))  # Output: Isosceles
print("Sides 3, 4, 5:", triangle_type(3, 4, 5))  # Output: Scalene
