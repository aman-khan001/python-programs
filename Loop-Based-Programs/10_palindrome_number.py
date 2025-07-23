# 📚 Python Program: Palindrome Number Check


'''
    The is_palindrome function takes an integer n as input and returns True if n is a palindrome, otherwise False.
    It reverses the number using a while loop and compares it with the original number.
'''

def is_palindrome(n):
    original = n
    reversed_num = 0
    
    # Handle negative numbers
    while n > 0:
        # Extract the last digit and build the reversed number
        digit = n % 10
        # Update the reversed number
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return original == reversed_num

# Example usage
n = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
# Example output:
# Enter a number to check if it is a palindrome: 121
# 121 is a palindrome.