# 📚 Python Program: Prime Number Check
# This program defines a function to check if a given integer is a prime number using a loop.

'''
    The is_prime function takes an integer n as input and returns True if n is a prime number, otherwise False.
    It checks for factors from 2 to the square root of n.
'''

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number other than 1 and itself, it is not prime
        if n % i == 0:
            return False
    # If no factors found, n is prime
    return True

# Example usage
n = int(input("Enter a number to check if it is prime: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
# Example output:
# Enter a number to check if it is prime: 7
# 7 is a prime number.
    