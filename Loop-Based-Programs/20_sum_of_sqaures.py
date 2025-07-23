# 📚 Python Program: Sum of Squares

'''
    The sum_of_squares function takes a positive integer n as input and returns the sum of squares of all integers from 1 to n.
    It uses a for loop to iterate through the numbers and calculates the square of each number, adding it to the total sum.
'''

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        # Calculate the square of the current number and add it to the total
        total += i * i
    return total

# Example usage
n = int(input("Enter a positive integer: "))
print(f"The sum of squares from 1 to {n} is: {sum_of_squares(n)}")
# Example output:
# Enter a positive integer: 5
# The sum of squares from 1 to 5 is: 55
