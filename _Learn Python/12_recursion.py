# 📘 Program: Recursive Function Example
# This program demonstrates how recursion works by calculating factorial of a number

'''
    A recursive function is a function that calls itself to solve smaller instances of the same problem.
    It typically has a base case to stop the recursion and a recursive case to continue the recursion.
    Recursion can be used to solve problems like calculating factorial, Fibonacci series, etc.
'''

# Defining a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: multiply n by factorial of (n-1)

# Taking input from the user
num = int(input("Enter a number: "))

# Calculating and displaying the factorial
print("Factorial of", num, "is", factorial(num))

# 🧠 How it works:
# Suppose the input is 4, it calls factorial(4):
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (base case)
# So, factorial(4) = 4 * 3 * 2 * 1 = 24
