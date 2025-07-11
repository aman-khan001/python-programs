# 📘 Program: Insertion Sort Algorithm
# This program demonstrates how to sort a list using insertion sort

'''
  Insertion sort is a simple sorting algorithm that builds a sorted array one element at a time.
  It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
'''



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Unsorted list
data = [12, 11, 13, 5, 6]
print("Original list:", data)

# Sorting the list
insertion_sort(data)
print("Sorted list:", data)

# 🧠 Explanation:
# Insertion sort builds the final sorted array one item at a time.
# It picks an element and inserts it into its correct position in the sorted part.
# Time complexity: O(n^2) in worst case, but efficient for nearly sorted data.
