# 📘 Program: Linear Search Algorithm
# This program demonstrates how to search for an element using linear search

'''
  A linear search is a simple algorithm that checks each element in a list sequentially until the target element is found or the end of the list is reached.
'''


def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Element found at this index
    return -1  # Element not found

# Sample list and target element
data = [5, 3, 8, 6, 7]
target = 6

# Searching and displaying the result
result = linear_search(data, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")

# 🧠 Explanation:
# Linear search checks each element one by one from start to end.
# Time complexity is O(n), where n is the length of the list.
# 📝 Note:
# This is simple but inefficient for large datasets.
# For better performance with large datasets, consider using binary search or hash tables.
