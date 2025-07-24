# 📚 Python Program to Flatten a Nested List

'''
  This program flattens a nested list into a single list.
'''

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # Recursively flatten sublists
        else:
            flat_list.append(item)  # Add non-list items directly
    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, [5, 6]], 7]
flattened = flatten_list(nested_list)
print("Original Nested List:", nested_list)
print("Flattened List:", flattened)

# 🧠 Explanation:
# The function `flatten_list` takes a nested list as input and returns a flattened version of it.
# It initializes an empty list `flat_list` to store the flattened items.
# The function iterates through each item in the input list and checks if it's a list itself.
# If it is, it recursively calls `flatten_list` on that sublist and extends `flat_list` with the result.
# If the item is not a list, it appends it directly to `flat_list`.
# Finally, it returns the flattened list.