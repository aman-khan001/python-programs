# 📚 Python Program to Replace All Occurrences of a Value in a List

'''  
  This program replaces all occurrences of a specified value in a list with a new value.
'''

def replace_all(lst, old_value, new_value):
    # Using list comprehension to create a new list with replaced values
    return [new_value if item == old_value else item for item in lst]

# Example usage
my_list = [1, 2, 3, 2, 4, 2]
old_value = 2
new_value = 5
print("Original list:", my_list)
print("Modified list:", replace_all(my_list, old_value, new_value)) 

# 🧠 Explanation:
# The function replace_all takes a list and replaces all occurrences of old_value with new_value.
# It uses a list comprehension to create a new list with the modified values.