# 📚 Python Program to Print an Inverted Right-Angled Triangle Pattern


def inverted_right_triangle(n):
    # Loop through each row
    for i in range(n, 0, -1):
        # Print '*' i times for the current row
        print('*' * i)

# Example usage
n = int(input("Enter the number of rows for the inverted right-angled triangle: "))
inverted_right_triangle(n)

# Example output:
# Enter the number of rows for the inverted right-angled triangle: 5
# *****
# ****
# ***
# **
# *