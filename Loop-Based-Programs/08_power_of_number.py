# 📚 Python Program: Power Calculation


'''
    The power function takes two integers, base and exponent, as input and returns the result of base raised to the power of exponent.
    It uses a for loop to multiply the base by itself for the number of times specified by the exponent.
'''

def power(base, exponent):
    """Calculate the power of a number using a loop."""
    # Check if exponent is negative
    result = 1
    # If exponent is negative, return an error message
    if exponent < 0:
        return "Exponent should be a non-negative integer"
    # Calculate base raised to the power of exponent
    for _ in range(exponent):
        # Multiply result by base for each iteration
        result *= base
    # Return the final result
    return result

# Example usage
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exponent} is: {power(base, exponent)}")
# Example output:
# Enter the base number: 2
# Enter the exponent: 3
# 2 raised to the power of 3 is: 8