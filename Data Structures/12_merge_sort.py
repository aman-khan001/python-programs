# 📘 Program: Merge Sort Algorithm
# This program demonstrates how to sort a list using the merge sort algorithm

'''
  Merge sort is a divide-and-conquer algorithm that splits the list into halves, sorts each half, and then merges them back together in sorted order.
'''


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking for any leftover elements
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Unsorted list
data = [38, 27, 43, 3, 9, 82, 10]
print("Original list:", data)

# Sorting the list
merge_sort(data)
print("Sorted list:", data)

# 🧠 Explanation:
# Merge Sort uses divide-and-conquer: divide the array, sort both halves, and merge them.
# Time complexity: O(n log n), stable and efficient for large data.
