# 📚 Python Program to Print a Pyramid Pattern

def pyramid_pattern(n):
    # Loop through each row
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
        '''
        Print spaces for alignment and '*' for the pyramid
        ' ' * (n - i) creates the leading spaces
        '*' * (2 * i - 1) prints the stars for the current row
        This ensures that the number of stars increases by 2 for each row
        '''

# Example usage
n = int(input("Enter the number of rows for the pyramid pattern: "))
pyramid_pattern(n)

# Example output:
# Enter the number of rows for the pyramid pattern: 5
#     *
#    ***
#   *****
#  *******
# *********