# 📚 Python Program: Simple Calculator

'''
  This program implements a simple calculator that can perform addition, subtraction,
  multiplication, and division. It prompts the user for two numbers and the desired operation,
  then calculates and displays the result. It also handles invalid inputs and division by zero.
'''

def calculator():
    print("Welcome to the Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the operation from the user
    operation = input("Please enter the operation you want to perform: ")

    # Validate the operation input
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please try again.")
        return

    # Get the numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2

    print(f"The result of {num1} {operation} {num2} is: {result}")

calculator()
# Example usage
# Welcome to the Calculator!
# Available operations:
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# Please enter the operation you want to perform: + 
# Enter the first number: 10
# Enter the second number: 5
# The result of 10.0 + 5.0 is: 15.0
