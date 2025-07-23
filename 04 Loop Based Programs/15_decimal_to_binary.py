# 📚 Python Program: Decimal to Binary Conversion


'''
    The decimal_to_binary function takes a non-negative integer n as input and returns its binary representation as a string.
    It uses a while loop to repeatedly divide n by 2 and collect the remainders.
'''

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        # Get the remainder when n is divided by 2
        remainder = n % 2
        # Append the remainder to the binary string
        binary = str(remainder) + binary
        # Update n by dividing it by 2
        n //= 2
    
    return binary

# Example usage
n = int(input("Enter a non-negative integer: "))
binary_representation = decimal_to_binary(n)
print(f"The binary representation of {n} is: {binary_representation}")
# Example output:
# Enter a non-negative integer: 10
# The binary representation of 10 is: 1010