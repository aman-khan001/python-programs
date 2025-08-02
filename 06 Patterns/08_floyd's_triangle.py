# 📚 Python Program to Print Floyd's Triangle Pattern

def floyds_triangle(n):
    """Prints Floyd's triangle pattern with n rows."""
    num = 1
    # Loop through each row
    for i in range(1, n + 1):
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            # Print the current number and increment it
            print(num, end=' ')
            num += 1
        print()  # Move to the next line after each row

# Example usage
n = int(input("Enter the number of rows for Floyd's triangle: "))
floyds_triangle(n)

# Example output:
# Enter the number of rows for Floyd's triangle: 5
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15