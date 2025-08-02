# 📚 Python Program to Print a Repeated Alphabet Triangle


def repeated_alphabet_triangle(n):
    """Prints a repeated alphabet triangle pattern with n rows."""
    for i in range(1, n + 1):
        # Print the ith letter repeated i times
        print((chr(64 + i) + ' ') * i)
        '''
        chr(64 + i) converts the row number to the corresponding uppercase letter (A=65, B=66, etc.)
        (chr(64 + i) + ' ') * i creates the repeated pattern for the current row
        '''

# Example usage
n = int(input("Enter the number of rows for the repeated alphabet triangle: "))
repeated_alphabet_triangle(n)

# Example output:
# Enter the number of rows for the repeated alphabet triangle: 5
# A
# B B
# C C C
# D D D D
# E E E E E