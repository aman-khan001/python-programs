# 📚 Python Program to Count Even and Odd Numbers in a List

'''  
  This program counts the number of even and odd numbers in a list.
'''

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        # Check if the number is even or odd
        if num % 2 == 0:
            # Increment even count if the number is even
            even_count += 1
        else:
            # Increment odd count if the number is odd
            odd_count += 1
    return even_count, odd_count

# Example usage
my_list = [1, 2, 3, 4, 5, 6]
evens, odds = count_even_odd(my_list)
print("Even numbers:", evens)
print("Odd numbers:", odds)

# 🧠 Explanation:
# The count_even_odd function takes a list of numbers as input and counts the even and odd numbers.
# It iterates through the list, checking each number's parity using the modulo operator.
# The function returns the counts of even and odd numbers.
