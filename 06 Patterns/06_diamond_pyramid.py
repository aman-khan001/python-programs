# 📚 Python Program to Print a Diamond Pyramid Pattern

def diamond_pyramid(n):
    # Print the upper part of the diamond (pyramid)
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    # Print the lower part of the diamond (inverted pyramid)
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
        '''
        Print spaces for alignment and '*' for the inverted pyramid
        ' ' * (n - i) creates the leading spaces
        '*' * (2 * i - 1) prints the stars for the current row
        This ensures that the number of stars decreases by 2 for each row
        '''

# Example usage
n = int(input("Enter the number of rows for the diamond pyramid: "))
diamond_pyramid(n)

# Example output:
# Enter the number of rows for the diamond pyramid: 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *