# 📚 Python Program to Reverse a List


def reverse_list(lst):
    reversed_list = []
    for item in lst:
        # Insert each item at the beginning of the new list
        reversed_list.insert(0, item)
    return reversed_list

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Reversed list is:", reverse_list(my_list)) 

# 🧠 Explanation:
# The function reverse_list takes a list as input and returns a new list that is the reverse of the original.
# It uses a for loop to iterate through the original list and inserts each element at the beginning of a new list.
# This effectively reverses the order of elements.