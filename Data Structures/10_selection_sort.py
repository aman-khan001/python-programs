# 📚 Python Program to Selection Sort Algorithm


'''
  Selection sort is a simple sorting algorithm that divides the input list into two parts:
    a sorted part and an unsorted part. It repeatedly selects the smallest (or largest) element
    from the unsorted part and moves it to the end of the sorted part.
'''



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Unsorted list
data = [29, 10, 14, 37, 13]
print("Original list:", data)

# Sorting the list
selection_sort(data)
print("Sorted list:", data)

# 🧠 Explanation:
# Selection sort finds the smallest element and places it at the beginning.
# Repeats for the rest of the list. Time complexity: O(n^2)
