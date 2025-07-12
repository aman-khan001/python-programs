# 🐥 Program: Defining and Using Functions
# This program demonstrates how to create and use functions in Python

''' 
A function is a block of reusable code that performs a specific task.
'''

# Defining a function that greets a user by name
def greet(name):
    print("Hello,", name + "!")  # Prints a greeting message

# Calling the function with an argument
greet("Oliver")  # Output: Hello, Oliver!

def add_numbers(a, b):
    return a + b  # Returns the sum of a and b

# Storing the result of the function
result = add_numbers(10, 20)
print("Sum:", result)  # Output: Sum: 30

# Defining a function with default parameters
def greet_with_default(name="Guest"):
    print("Hello,", name + "!")  # Prints a greeting message with a default name
# Calling the function without an argument
greet_with_default()  # Output: Hello, Guest!


# Types of function in python:
# 1. Built-in functions - Functions that are pre-defined in Python, like print(), len(), etc.
def built_in_example():
    print("This is a built-in function example.") # This function demonstrates the use of a built-in function (print).
   
# 2. User-defined functions - Functions that are defined by the user using the def keyword.
def user_defined_example(a, b):
    return a + b  # This function demonstrates the use of a user-defined function.