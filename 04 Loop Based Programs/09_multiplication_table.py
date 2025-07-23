# 📚 Python Program: Multiplication Table


'''
    The multiplication_table function takes an integer n as input and prints the multiplication table for n from 1 to 10.
    It uses a for loop to iterate through numbers 1 to 10 and prints the product of n and each number.
'''

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
# Example usage
n = int(input("Enter a number to generate its multiplication table: "))
multiplication_table(n)
# Example output:
# Enter a number to generate its multiplication table: 5  
# 5 x 1 = 5 
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50