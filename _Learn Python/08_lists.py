# 🐥 Program: Working with Lists


'''
    A list is a collection of data/elements.
    Lists are ordered, mutable/changeable, and allow duplicate values.
    Lists are defined using square brackets [] and can contain any data type.
    Lists can be used to store multiple items in a single variable.
'''

# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# Printing the entire list
print("Fruits:", fruits)  # Output: ['apple', 'banana', 'cherry']


# List operations and methods

# 1. append() - Adds an item to the end of the list
fruits.append("orange")
print("After append:", fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 2. extend() - Adds all items from another list to the current list
fruits.extend(["grape", "pineapple"])
print("After extend:", fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'pineapple']

# 3. insert() - Inserts an item at a specific position
fruits.insert(2, "kiwi")  # Adds 'kiwi' at index 2
print("After insert:", fruits)  # Output: ['apple', 'banana', 'kiwi', 'cherry', 'orange', 'grape', 'pineapple']

# 4. remove() - Removes the first occurrence of a specified item
fruits.remove("banana")
print("After remove:", fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange', 'grape', 'pineapple']

# 5. pop() - Removes and returns an item at a specific position (default is the last item)
removed_item = fruits.pop()
print("After pop:", fruits)  # Output: ['apple', 'kiwi', 'cherry', 'orange', 'grape']
print("Removed item:", removed_item)  # Output: pineapple

# 6. clear() - Removes all items from the list
fruits.clear()
print("After clear:", fruits)  # Output: []

# Recreating the list for further examples
fruits = ["apple", "banana", "cherry", "apple"]

# 7. index() - Returns the index of the first occurrence of a specified item
index_of_cherry = fruits.index("cherry")
print("Index of 'cherry':", index_of_cherry)  # Output: 2

# 8. count() - Returns the number of occurrences of a specified item
count_of_apple = fruits.count("apple")
print("Count of 'apple':", count_of_apple)  # Output: 2

# 9. sort() - Sorts the list in ascending order
fruits.sort()
print("After sort:", fruits)  # Output: ['apple', 'apple', 'banana', 'cherry']

# 10. reverse() - Reverses the order of the list
fruits.reverse()
print("After reverse:", fruits)  # Output: ['cherry', 'banana', 'apple', 'apple']

# 11. copy() - Creates a shallow copy of the list
fruits_copy = fruits.copy()
print("Original list:", fruits)
print("Copied list:", fruits_copy)


# Checking if an item exists in the list
print("Is 'apple' in the list?", "apple" in fruits)  # Output: True

# Iterating through the list
print("All fruits:")
for fruit in fruits:
    print("-", fruit)

# List slicing - Getting a subset of the list
sliced_fruits = fruits[1:3]  # Getting items from index 1 to 2
print("Sliced fruits:", sliced_fruits)  # Output: ['banana', 'cherry']

# List length - Getting the number of items in the list
print("Number of fruits:", len(fruits))  # Output: 4
