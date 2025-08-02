# 📚 Python Program to Print an Inverted Pyramid Pattern

def inverted_pyramid(n):
    # Loop through each row
    for i in range(n, 0, -1):
        # Print spaces for alignment
        print(' ' * (n - i), end='')
        # Print '*' i times for the current row
        print('*' * (2 * i - 1))
        '''
        Print spaces for alignment and '*' for the inverted pyramid
        ' ' * (n - i) creates the leading spaces
        '*' * (2 * i - 1) prints the stars for the current row
        This ensures that the number of stars decreases by 2 for each row
        '''

# Example usage
n = int(input("Enter the number of rows for the inverted pyramid: "))
inverted_pyramid(n) 

# Example output:
# Enter the number of rows for the inverted pyramid: 5
# *********
#  *******
#   *****
#    ***
#     *