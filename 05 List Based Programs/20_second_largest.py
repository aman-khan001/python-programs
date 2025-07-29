# 📚 Python Program to Find the Second Largest Number in a List

'''  
  This program finds the second largest number in a list of numbers.
'''

def second_largest(numbers):
    # Find the largest number
    largest = max(numbers)
    # Remove the largest number from the list
    numbers.remove(largest)
    # Find the second largest number
    second_largest = max(numbers)
    return second_largest

# Example usage
my_list = [1, 2, 3, 4, 5]
print("The second largest number is:", second_largest(my_list))

# 🧠 Explanation:
# The function second_largest takes a list of numbers as input.
# It first finds the largest number using the max function.
# Then, it removes the largest number from the list to ensure that the second largest can be found.
# Finally, it finds and returns the second largest number using the max function again.