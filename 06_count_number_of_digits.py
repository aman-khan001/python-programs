# 📚 Python Program: Count Number of Digits
# This program defines a function to count the number of digits in a given integer using a while loop.

'''
    The count_digits function takes an integer n as input and returns the number of digits in n.
    It uses a while loop to repeatedly divide n by 10 until n becomes 0, counting the number of iterations.
'''

def count_digits(n):
    # Initialize digit count to 0
    digit_count = 0
    # Handle negative numbers by taking absolute value
    n = abs(n)
    
    # Loop until n becomes 0
    while n > 0:
        # Remove the last digit from n
        n //= 10
        # Increment the digit count
        digit_count += 1
    
    return digit_count

# Example usage
n = int(input("Enter an integer: "))
print(f"The number of digits in {n} is: {count_digits(n)}")
# Example output:
# Enter an integer: 12345
# The number of digits in 12345 is: 5
