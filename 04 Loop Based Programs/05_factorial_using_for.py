# 📚 Python Program: Factorial Calculation

'''
    The factorial function takes a non-negative integer n as input and returns the factorial of n.
    It uses a for loop to multiply all integers from 2 to n.
'''

def factorial(n):
    # Check if n is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # Initialize result to 1
    result = 1
    # Calculate factorial using a for loop
    for i in range(2, n + 1):
        # Multiply result by i
        result *= i
    return result

# Example usage
n = int(input("Enter a non-negative integer: "))
print(f"The factorial of {n} is: {factorial(n)}")
# Example output:
# Enter a non-negative integer: 5
# The factorial of 5 is: 120