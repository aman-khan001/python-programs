# 📘 Program: Quick Sort Algorithm
# This program demonstrates how to sort a list using the quick sort algorithm

'''
    Quick sort is a highly efficient sorting algorithm and is based on partitioning an array into smaller sub-arrays.
    A pivot element is chosen, and the array is partitioned into elements less than or equal to the pivot and elements greater than the pivot.  
'''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choose the first element as pivot
        less = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
        greater = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Unsorted list
data = [10, 7, 8, 9, 1, 5]
print("Original list:", data)

# Sorting the list
data = quick_sort(data)
print("Sorted list:", data)

# 🧠 Explanation:
# Quick Sort picks a pivot, partitions the list into less and greater, and recursively sorts them.
# Time complexity: O(n log n) on average, but worst case is O(n^2).
# It's efficient for large datasets and often used in practice.
