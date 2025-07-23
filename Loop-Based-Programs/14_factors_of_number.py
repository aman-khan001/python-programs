# 📚 Python Program: Factors of a Number


'''
    The print_factors function takes a positive integer n as input and prints all its factors.
    It loops through all numbers from 1 to n and checks if they are factors of n.
'''

def print_factors(n):
    """Print all factors of a given number n."""
    # Check if n is less than or equal to 0
    if n <= 0:
        print("Please enter a positive integer.")
        return
    # Loop through all numbers from 1 to n
    for i in range(1, n + 1):
        # If i is a factor of n, print it
        if n % i == 0:
            print(i)

# Example usage
n = int(input("Enter a positive integer to find its factors: "))

print(f"The factors of {n} are:")
print_factors(n)
# Example output:
# Enter a positive integer to find its factors: 12
# The factors of 12 are:
# 1
# 2
# 3
# 4
# 6
# 12
