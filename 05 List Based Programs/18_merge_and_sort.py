# 📚 Python Program to Merge and Sort Two Lists

'''  
  This program merges two lists and sorts the resulting list in ascending order.
'''

def merge_and_sort_lists(list1, list2):
    # Merge the two lists
    merged_list = list1 + list2
    # Sort the merged list in ascending order
    return merged_list.sort()

# Example usage
list1 = [3, 1, 4, 2]
list2 = [6, 5, 8, 7]
sorted_list = merge_and_sort_lists(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Merged and Sorted List:", sorted_list)

# 🧠 Explanation:
# The function merge_and_sort_lists takes two lists as input, merges them, and sorts the merged list in ascending order.
# It uses the sort() method to arrange the elements in the desired order.