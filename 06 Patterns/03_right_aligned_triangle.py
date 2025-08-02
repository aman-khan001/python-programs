# 📚 Python Program to Print a Right-Aligned Triangle Pattern

def right_aligned_triangle(n):
    # Loop through each row
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
        '''
        Print spaces for alignment and '*' for the triangle
        ' ' * (n - i) creates the leading spaces
        '*' * i prints the stars for the current row
        '''

# Example usage
n = int(input("Enter the number of rows for the right-aligned triangle: "))
right_aligned_triangle(n)

# Example output:
# Enter the number of rows for the right-aligned triangle: 5
#     *
#    **
#   ***
#  ****
# *****