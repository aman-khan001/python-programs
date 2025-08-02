# 📚 Python Program to Print an Alphabet Pyramid Pattern

def alphabet_pyramid(rows: int):
    """Prints an alphabet pyramid pattern with the specified number of rows."""
    # Loop through each row
    for i in range(rows):
        # Print leading spaces for pyramid shape
        print(" " * (rows - i - 1), end="")
        ch = 65 # ASCII value of 'A'
        # Print characters in the current row
        for j in range(2 * i + 1):
            # Print the character corresponding to the current ASCII value
            print(chr(ch), end="")
            ch += 1 # Increment the character for the next position
        print() # Move to the next line after each row

# Example usage
n = int(input("Enter the number of rows for the alphabet pyramid: "))
alphabet_pyramid(n)

# Example output:
# Enter the number of rows for the alphabet pyramid: 5
#    A
#   ABC
#  ABCDE
# ABCDEFG