# 📚 Python Program to Find the Second Largest Number in a List

'''
  This program finds the second largest number in a list of numbers.
'''

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest

    first = second = float('-inf')  # Initialize to negative infinity

    for num in numbers:
        if num > first:
            second = first  # Update second largest
            first = num  # Update largest
        elif num > second and num != first:
            second = num  # Update second largest if it's not equal to the largest

    return second if second != float('-inf') else None  # Return None if no second largest found

# Example usage
numbers = [3, 5, 1, 8, 2]
second_largest = find_second_largest(numbers)
if second_largest is not None:
    print(f"The second largest number in the list is: {second_largest}")
else:
    print("The list does not have a second largest number.")

# 🧠 Explanation:
# The function `find_second_largest` takes a list of numbers as input and returns the second largest number in the list.
# It initializes two variables, `first` and `second`, to negative infinity.
# It iterates through the list, updating `first` and `second` as it finds larger numbers.
# Finally, it returns the second largest number found or None if there is no second largest.