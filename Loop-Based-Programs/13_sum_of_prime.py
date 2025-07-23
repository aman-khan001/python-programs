# 📚 Python Program: Sum of Prime Numbers


'''
    The sum_of_prime function takes a positive integer n as input and returns the sum of all prime numbers up to n.
    It uses a nested function is_prime to check if each number is prime.
'''

def sum_of_prime(n):
    """Calculate the sum of all prime numbers up to n."""
    def is_prime(num):
        """Check if a number is prime."""
        # Check if num is less than or equal to 1
        if num <= 1:
            return False
        # Check for factors from 2 to the square root of num
        for i in range(2, int(num**0.5) + 1):
            # If num is divisible by any number other than 1 and itself, it is not prime
            if num % i == 0:
                return False
        # If no factors found, num is prime
        return True

    # Initialize total to 0
    total = 0
    # Loop through all numbers from 2 to n
    for i in range(2, n + 1):
        # If i is prime, add it to the total
        if is_prime(i):
            total += i
    # Return the total sum of prime numbers
    return total

# Example usage
n = int(input("Enter a positive integer: "))
print(f"The sum of all prime numbers up to {n} is: {sum_of_prime(n)}")
# Example output:
# Enter a positive integer: 10
# The sum of all prime numbers up to 10 is: 17 (2 + 3 + 5 + 7 = 17)