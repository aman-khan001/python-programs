# 📚 Python Program to Find the Largest of Three Integers Using Nested If Statements


'''
    The nested_largest function takes three integers as input
    and returns the largest integer among them.
    It uses nested conditional statements to compare the integers.
'''

def nested_largest(a, b, c):
    
    if a >= b:
        # If a is greater than or equal to b, compare a with c
        if a >= c:
            return a
        else:
            return c
    else:
        # If b is greater than a, compare b with c
        if b >= c:
            return b
        else:
            return c
        
# Example usage
print("Largest of 3, 5, and 2:", nested_largest(3, 5, 2))  # Output: 5
print("Largest of 10, 20, and 15:", nested_largest(10, 20, 15))  # Output: 20