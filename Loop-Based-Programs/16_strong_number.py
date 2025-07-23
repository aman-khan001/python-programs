# 📚 Python Program: Strong Number Check



'''
    A strong number is a number whose sum of the factorials of its digits is equal to the number itself.

    The is_strong function checks if a given number is a strong number.
    It calculates the sum of the factorials of its digits and compares it to the original number.
'''


def is_strong(num):
    # Helper function to calculate factorial of a number
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        # Calculate factorial iteratively
        for i in range(2, n + 1):
            result *= i
        return result
    # Calculate the sum of the factorials of the digits
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    # Check if the sum of factorials equals the original number
    return sum_of_factorials == num

# Example usage
number = int(input("Enter a number: "))
if is_strong(number):
  print(f"{number} is a strong number.")
else:
  print(f"{number} is not a strong number.")
  
# Example output:
# Enter a number: 145 
# 145 is a strong number. (1! + 4! + 5! = 1 + 24 + 120 = 145)
# Enter a number: 123
# 123 is not a strong number.
