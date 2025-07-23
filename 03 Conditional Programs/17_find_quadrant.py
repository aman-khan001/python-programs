# 📚 Python Program to Find Quadrant of a Point in Cartesian Coordinate System


'''
    The find_quadrant function takes the x and y coordinates of a point as input
    and returns the quadrant in which the point lies.
    It uses conditional statements to determine the quadrant based on the signs of x and y.
'''

def find_quadrant(x, y):
    """
    This function determines the quadrant of a point (x, y) in a Cartesian coordinate system.
    
    Parameters:
    x (float): The x-coordinate of the point.
    y (float): The y-coordinate of the point.
    
    Returns:
    str: A string indicating the quadrant of the point.
    """
    if x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    elif x > 0 and y < 0:
        return "Quadrant IV"
    else:
        return "Point is on an axis or at the origin"
    
# Example usage
print("Find Quadrant:")
print("Point (3, 4) is in", find_quadrant(3, 4))    # Output: Quadrant I
print("Point (-2, 5) is in", find_quadrant(-2, 5))   # Output: Quadrant II
print("Point (-3, -4) is in", find_quadrant(-3, -4)) # Output: Quadrant III