
def hollow_square(n):
    """
    # Hollow Square Pattern
    Prints a hollow square pattern with n rows and n columns.

    ## Arguments
    - n: int, size of the square

    ## Example
    Input:
        n = 5
    Output:
        * * * * *
        *       *
        *       *
        *       *
        * * * * *
    """
    for i in range(n):
        for j in range(n):
            # Print '*' for the border cells (first/last row or column)
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # Next line after each row

# Example usage
n = int(input("Enter the size of the hollow square: "))
hollow_square(n)






