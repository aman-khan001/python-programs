# 📚 Python Program: Factorial Calculation

'''
    The factorial function takes a non-negative integer n as input and returns the factorial of n.
    It uses a while loop to multiply all integers from n down to 1.
'''

def factorial(n):
    # Check if n is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"
    # Initialize result to 1
    result = 1
    # Calculate factorial using a while loop
    while n > 1:
        # Multiply result by n and decrement n
        result *= n
        n -= 1
    return result

# Example usage
n = int(input("Enter a non-negative integer: "))
print(f"The factorial of {n} is: {factorial(n)}")
# Example output:
# Enter a non-negative integer: 5
# The factorial of 5 is: 120
