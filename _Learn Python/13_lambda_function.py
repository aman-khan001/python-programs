# 📘 Program: Lambda Functions in Python
# This program demonstrates how to use lambda (anonymous) functions

'''
  A lambda function is a small anonymous function defined with the lambda keyword.  
  It can take any number of arguments but can only have one expression.
  Lambda functions are often used for short, throwaway functions that are not reused elsewhere.
'''

# A regular function to add two numbers
def add(a, b):
    return a + b

print("Regular add:", add(5, 3))  # Output: 8

# A lambda function that does the same thing
lambda_add = lambda a, b: a + b
print("Lambda add:", lambda_add(5, 3))  # Output: 8

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4, 6]

# 🧠 Explanation:
# lambda a, b: a + b → defines a one-line function that returns the sum of a and b
# filter(lambda x: x % 2 == 0, numbers) → keeps only even numbers from the list
