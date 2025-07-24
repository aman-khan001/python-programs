# 📚 Python Program to Find Common Elements in Two Lists

'''  
  This program finds common elements between two lists.
'''

def find_common_elements(list1, list2):
    # Find common elements between two lists
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Common Elements:", common_elements)  

# 🧠 Explanation:
# The function `find_common_elements` takes two lists as input and returns a list of common elements.
# It converts both lists to sets and finds their intersection using the `&` operator.
# The result is then converted back to a list before being returned.

