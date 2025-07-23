# 📚 Python Program to Swap Two Numbers

'''
    The swap function takes two numbers as inputs and swaps them using arithmetic operations.
    It avoids using a temporary variable for the swap.
'''

def swap(a, b):
    # Swap two numbers using arithmetic operations
    if a == b:
        return a, b
    
    # Using arithmetic operations to swap
    a = a + b
    b = a - b
    a = a - b
    return a, b

    # Alternatively, you can use tuple unpacking to swap
    # a, b = b, a
    # return a, b

# Example usage
print("Before swapping: a = 5, b = 10")
a, b = swap(5, 10)
print("After swapping: a =", a, ", b =", b)  # Output: a = 10 , b = 5

# 🧠 Explanation:
# The swap function swaps two numbers using arithmetic operations.
# It adds the two numbers, then subtracts the second from the sum to get the first,
# and finally subtracts the new second from the sum to get the second.
# This method avoids using a temporary variable for swapping.
