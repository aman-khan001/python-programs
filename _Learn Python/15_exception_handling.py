# 📘 Program: Exception Handling in Python
# This program demonstrates how to handle errors using try-except blocks
'''
Exception handling is a mechanism to gracefully handle errors that may occur during program execution.
It allows the program to continue running even if an error occurs, instead of crashing.
Exception handling is done using try-except blocks.
The code inside the try block is executed, and if an error occurs, the control is transferred to the except block.
This is useful for handling runtime errors like division by zero, file not found, etc.
'''



# Taking two numbers from the user
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    # Attempting to divide the numbers
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")  # Handles division by zero

except ValueError:
    print("❌ Error: Please enter valid integers.")  # Handles non-integer input

# This block runs no matter what
finally:
    print("✅ Program completed.")
