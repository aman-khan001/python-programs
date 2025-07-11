# 📚 Python Program to Check Divisibility by 3 or 5
# This program defines a function to check if a number is divisible by 3 or 5.

'''
    The divisible_by_3_or_5 function takes an integer as input and returns a string indicating
    whether the number is divisible by 3, 5, both, or neither.
'''

def divisible_by_3_or_5(n):
    if n % 3 == 0 or n % 5 == 0:
        return "Divisible by 3 or 5"
    elif n % 3 == 0:
        return "Divisible by 3"
    elif n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 3 or 5"
    
# Example usage
print("Check 9:", divisible_by_3_or_5(9))   # Output: Divisible by 3
print("Check 10:", divisible_by_3_or_5(10)) # Output: Divisible by 5
print("Check 15:", divisible_by_3_or_5(15)) # Output: Divisible by 3 or 5
print("Check 7:", divisible_by_3_or_5(7))   # Output: Not divisible by 3 or 5