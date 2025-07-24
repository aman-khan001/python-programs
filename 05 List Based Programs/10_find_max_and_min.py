# 📚 Python Program to Find Maximum and Minimum in a List

'''  
  This program finds the maximum and minimum numbers in a list of numbers.
'''

def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None if the list is empty

    # Initialize max and min with the first element
    max_num = min_num = numbers[0]

    # Iterate through the list to find max and min
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_num, min_num = find_max_min(numbers)
print("List of numbers:", numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)