# 📚 Python Program to Merge Two Sorted Lists

'''
  This program merges two sorted lists into a single sorted list.
'''

def merge_lists(list1, list2):
    # Initialize an empty list to store the merged elements
    merged_list = []
    # Initialize pointers for both lists
    i, j = 0, 0
    # Iterate until we reach the end of either list
    while i < len(list1) and j < len(list2):
        # Compare elements from both lists and append the smaller one
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Append any remaining elements from either list
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    # Return the merged list
    return merged_list

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = merge_lists(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Merged List:", merged_list)

# 🧠 Explanation:
# The function `merge_lists` takes two sorted lists as input and returns a new list that merges them in sorted order.
# It initializes an empty list `merged_list` to store the merged items.
# The function uses two pointers to iterate through both lists and appends the smaller element to `merged_list`.
# Finally, it returns the merged list.