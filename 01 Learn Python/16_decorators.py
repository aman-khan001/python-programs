# 🐥 Program: Using Decorators in Python


'''    
    A decorator is a special type of function that can modify the behavior of another function.
    It is often used to add functionality to existing functions without modifying their code.
    Decorators are defined using the @ syntax and can be used to log, authenticate, or modify the output of functions.
'''

# Defining a decorator function
def my_decorator(func):
    def wrapper():
        print("Before the function is called")
        func()  # Call the original function
        print("After the function is called")
    return wrapper

# Using the decorator with @ syntax
@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# 🧠 Explanation:
# The decorator adds behavior before and after the original function.
# When say_hello() is called, it runs wrapper(), not just the print("Hello!") line.
# This allows us to add functionality (like logging, timing, etc.) without modifying the original function.
# Decorators can also take arguments, allowing for more complex behavior.
# Decorators are often used in web frameworks, logging, and access control.
