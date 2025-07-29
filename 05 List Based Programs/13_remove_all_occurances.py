# 📚 Python Program to Remove All Occurrences of a Value from a List

'''
  This program removes all occurrences of a specified value from a list and returns a new list.
'''

def remove_all_occurrences(lst, value):
    # Create a new list to store elements that are not equal to the value
    new_list = []
    # Iterate through the original list
    for item in lst:
        # If the item is not equal to the value, add it to the new list
        if item != value:
            new_list.append(item)
    return new_list

# Example usage
original_list = [1, 2, 3, 4, 2, 5]
value_to_remove = 2
new_list = remove_all_occurrences(original_list, value_to_remove)
print("Original list:", original_list)
print("List after removing all occurrences of", value_to_remove, ":", new_list)

# 🧠 Explanation:
# The remove_all_occurrences function takes a list and a value as input.
# It creates a new list to store elements that are not equal to the value.
# By iterating through the original list and checking each element,
# it effectively removes all occurrences of the specified value.
