# 📚 Python Program: Check Armstrong Number


'''
    An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''

def is_armstrong_number(num):
  original_num = num
  # Count the number of digits in the number
  num_digits = len(str(num))
  # Calculate the sum of each digit raised to the power of num_digits
  sum_of_powers = 0
  # Loop through each digit of the number
  while num > 0:
    # Get the last digit
    digit = num % 10
    # Add the digit raised to the power of num_digits to the sum
    sum_of_powers += digit ** num_digits
    # Remove the last digit from the number
    num //= 10
  # Check if the sum of powers is equal to the original number
  return sum_of_powers == original_num
# Example usage
num = int(input("Enter an integer: "))
# Check if the number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else: 
    print(f"{num} is not an Armstrong number.")
# Example output:
# Enter an integer: 153
# 153 is an Armstrong number.