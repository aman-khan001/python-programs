#  🐥 Program: Working with Tuples
#  This program demonstrates how to create and use tuples in Python


'''
    Tuples are similar to lists but are immutable (cannot be changed after creation).
    Tuples are defined using parentheses () and can contain any data type.
    Tuples are ordered, meaning the items have a defined order, and they can contain duplicate values.
'''

# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry")
# Printing the entire tuple
print("Fruits:", fruits)  # Output: ('apple', 'banana', 'cherry')


# Tuple methods
# 1. count() - Returns the number of occurrences of a specified item
count_of_apple = fruits.count("apple")

print("Count of 'apple':", count_of_apple)  # Output: 1

# 2. index() - Returns the index of the first occurrence of a specified item
index_of_banana = fruits.index("banana")



# Tuple operations 
'''
    Tuples are immutable, so we cannot modify them directly.
    However, we can perform some operations that return new tuples.
'''
# Accessing items - Tuples can be accessed using indexing
print("First fruit:", fruits[0])  # Output: apple

# Slicing - Tuples can be sliced to get a subset of items
print("First two fruits:", fruits[:2])  # Output: ('apple', 'banana')

# Concatenation - Tuples can be concatenated to create a new tuple
new_fruits = fruits + ("orange", "grape")
print("After concatenation:", new_fruits)  # Output: ('apple', 'banana', 'cherry', 'orange', 'grape')

# Repetition - Tuples can be repeated to create a new tuple
repeated_fruits = fruits * 2
print("After repetition:", repeated_fruits)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Checking membership - We can check if an item exists in a tuple
print("Is 'banana' in fruits?", "banana" in fruits)  # Output: True

# Finding length - We can find the number of items in a tuple
print("Number of fruits:", len(fruits))  # Output: 3

#  Iterating through a tuple - We can iterate through the items in a tuple 
for fruit in fruits:
    print("Fruit:", fruit)
# Output: Fruit: apple, Fruit: banana, Fruit: cherry
    