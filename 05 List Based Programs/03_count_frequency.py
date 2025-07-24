# 📚 Python Program to Count Frequency of Elements in a List

'''
  This program counts the frequency of each element in a list of numbers.
'''


def count_frequency(numbers):
    # Initialize an empty dictionary to store frequency
    frequency = {}
    # Iterate through the list and count occurrences
    for num in numbers:
        # Use get() to handle missing keys and increment the count
        frequency[num] = frequency.get(num, 0) + 1
    # Return the frequency dictionary
    return frequency

# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_count = count_frequency(numbers)
print("Frequency of elements in the list:")
for num, count in frequency_count.items():
    print(f"{num}: {count}")

# 🧠 Explanation:
# The function `count_frequency` takes a list of numbers as input and returns a dictionary with the frequency count of each number.
# It initializes an empty dictionary `frequency` to store the count of each element.
# The function iterates through the list, using the `get()` method to handle missing keys and increment the count.
# Finally, it returns the frequency dictionary.