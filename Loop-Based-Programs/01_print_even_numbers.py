# 📚 Python Program: Print Even Numbers

'''
     The print_even_numbers function takes an integer n as input and prints all even numbers from 0 to n (inclusive).
      It uses a for loop to iterate through the range from 0 to n, incrementing by 2 to ensure only even numbers are printed.
'''

def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

# Example usage
n = int(input("Enter a number: "))
print("Even numbers from 0 to", n, ":")
print_even_numbers(n)
