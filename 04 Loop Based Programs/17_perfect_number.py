# 📚 Python Program: Perfect Number Check


'''
    A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself).
    
    The is_perfect function checks if a given number is a perfect number.
    It calculates the sum of its divisors and compares it to the original number.
'''

def is_perfect(n):
    if n < 1:
        return False
    sum_of_divisors = 0
    # Loop through all numbers from 1 to n-1 to find divisors
    for i in range(1, n):
        # If i is a divisor of n, add it to the sum
        if n % i == 0:
            sum_of_divisors += i
    # Check if the sum of divisors equals the original number
    return sum_of_divisors == n

# Example usage
number = int(input("Enter a number: "))
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

# Example output:
# Enter a number: 6
# 6 is a perfect number. (1 + 2 + 3 = 6)
    
# Enter a number: 28
# 28 is a perfect number. (1 + 2 + 4 + 7 + 14 = 28)