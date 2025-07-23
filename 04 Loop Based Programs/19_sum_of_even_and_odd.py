# 📚 Python Program: Sum of Even and Odd Numbers


'''
    The sum_of_even_and_odd function takes a positive integer n as input and returns the sum of even and odd numbers from 1 to n.
    It uses a for loop to iterate through the numbers and checks if each number is even or odd, updating the respective sums accordingly.
'''

def sum_of_even_and_odd(n):
    even_sum = 0
    odd_sum = 0
    for i in range(1, n + 1):
        # Check if the number is even or odd
        if i % 2 == 0:
            # If even, add to even_sum
            even_sum += i
        else:
            odd_sum += i
    # Return the final sums
    return even_sum, odd_sum

# Example usage
n = int(input("Enter a positive integer: "))
even_sum, odd_sum = sum_of_even_and_odd(n)
print(f"Sum of even numbers from 1 to {n} is: {even_sum}")
print(f"Sum of odd numbers from 1 to {n} is: {odd_sum}")
# Example output:
# Enter a positive integer: 10
# Sum of even numbers from 1 to 10 is: 30
# Sum of odd numbers from 1 to 10 is: 25