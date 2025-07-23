# 📚 Python Program to Binary Search Algorithm


'''
  Binary search is an efficient algorithm for finding an item from a sorted list of items.
'''


# Binary search function
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Element not found

# Sorted list and target element
data = [2, 4, 6, 8, 10, 12, 14]
target = 10

# Perform binary search
result = binary_search(data, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")

# 🧠 Explanation:
# Binary search works on sorted arrays.
# It repeatedly divides the search interval in half.
# Time complexity is O(log n).
