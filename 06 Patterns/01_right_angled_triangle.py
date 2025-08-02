# 📚 Python Program: Right-Angled Triangle Pattern


def right_angled_triangle(n):
    # Loop through each row
    for i in range(1, n + 1):
        # Print '*' i times for the current row
        print('*' * i)

# Example usage
n = int(input("Enter the number of rows for the right-angled triangle: "))
right_angled_triangle(n)

# Example output:
# Enter the number of rows for the right-angled triangle: 5
# *
# **
# ***
# ****
# *****
# ******  
