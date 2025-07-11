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

    operation = input("Please enter the operation you want to perform: ")

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please try again.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

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
