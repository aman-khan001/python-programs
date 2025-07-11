# 📚 Python Program to Convert Kilometers to Miles
# This program defines a function to convert kilometers to miles.

'''
    The kilometers_to_miles function takes a distance in kilometers as input
    and returns the equivalent distance in miles using the conversion factor:
    1 kilometer = 0.621371 miles.
'''

def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# Example usage
print("Kilometers to Miles:")
print("10 km =", kilometers_to_miles(10), "miles")  # Output: 6.21371
print("100 km =", kilometers_to_miles(100), "miles")  # Output: 62.1371
