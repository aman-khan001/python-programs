# 🐣 Program: Conditional Statements in Python


''' Conditional statements allow the program to execute certain blocks of code based on specific conditions.'''

# Taking user input for age and converting it to integer
age = int(input("Enter your age: "))

# Checking the age using if-elif-else
if age < 13:
    print("You are a child.")  # Executes if age is less than 13
elif age < 20:
    print("You are a teenager.")  # Executes if age is between 13 and 19
elif age < 60:
    print("You are an adult.")  # Executes if age is between 20 and 59
else:
    print("You are a senior citizen.")  # Executes if age is 60 or above
