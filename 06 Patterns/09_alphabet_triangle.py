# 📚 Python Program to Print an Alphabet Triangle Pattern

def alphabet_triangle(n):
    """Prints an alphabet triangle pattern with n rows."""
    for i in range(1, n + 1):
        # Print letters from A to the ith letter
        for j in range(1, i + 1):
            print(chr(64 + j), end=' ')
        print()  # Move to the next line after each row

# Example usage
n = int(input("Enter the number of rows for the alphabet triangle: "))
alphabet_triangle(n)

# Example output:
# Enter the number of rows for the alphabet triangle: 5
# A
# A B
# A B C
# A B C D
# A B C D E