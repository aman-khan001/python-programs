# 📚 Python Program to Print a Number Triangle Pattern

def number_triangle(n):
    """Prints a number triangle pattern with n rows."""
    for i in range(1, n + 1):
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Move to the next line after each row

# Example usage
n = int(input("Enter the number of rows for the number triangle: "))
number_triangle(n)  

# Example output:
# Enter the number of rows for the number triangle: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5