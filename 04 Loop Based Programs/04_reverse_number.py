# 📚 Python Program: Reverse a Number


'''
    The reverse_number function takes an integer n as input and returns the reversed number.
    It uses a while loop to extract digits from n and build the reversed number.
'''

def reverse_number(n):
    # Initialize reversed number to 0
    reversed_num = 0
    # Loop until n becomes 0
    while n > 0:
        # Get the last digit of n
        digit = n % 10
        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from n
        n //= 10
    return reversed_num

# Example usage
n = int(input("Enter a number: "))
print(f"The reversed number is: {reverse_number(n)}")
# Example output:
# Enter a number: 12345
# The reversed number is: 54321