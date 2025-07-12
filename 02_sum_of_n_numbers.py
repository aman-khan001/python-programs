# 📚 Python Program: Sum of n Numbers
# This program defines a function to calculate the sum of all integers from 1 to n (inclusive).
  
'''
      The sum_of_n function takes an integer n as input and returns the sum of all integers from 1 to n (inclusive).
      It uses a for loop to iterate through the range from 1 to n, adding each integer to a total sum.
'''

def sum_of_n(n):
    # Initialize total to 0
    total = 0
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Add each number to total
        total += i
    # Return the total sum
    return total

# Example usage
n = int(input("Enter a number: "))
print(f"The sum of all integers from 1 to {n} is: {sum_of_n(n)}")
# Example output:
# Enter a number: 5
# The sum of all integers from 1 to 5 is: 15