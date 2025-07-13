# 📚 Python Program: Fibonacci Series
# This program defines a function to generate the Fibonacci series up to n terms using a loop.

'''
    The fibonacci_series function takes an integer n as input and returns a list containing the first n terms of the Fibonacci series.
    It uses a for loop to calculate each term based on the previous two terms.
'''

def fibonacci_series(n):
    a = 0
    b = 1
    # Initialize the Fibonacci series with the first two terms
    series = []
    # Loop to generate the Fibonacci series up to n terms
    for _ in range(n):
        # Append the current term to the series
        series.append(a)
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    return series

# Example usage
n = int(input("Enter the number of terms in the Fibonacci series: "))
fibonacci = fibonacci_series(n)
print(f"The first {n} terms of the Fibonacci series are: {fibonacci}")
# Example output:
# Enter the number of terms in the Fibonacci series: 10
# The first 10 terms of the Fibonacci series are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]