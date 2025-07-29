# 📚 Python Program to Count Frequency of Elements in a List

'''  
  This program counts the frequency of each element in a list of numbers.
'''


from collections import Counter


def count_frequency(elements):
    # Using Counter to count frequency of elements
    frequency = Counter(elements)
    return frequency

# Example usage
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = count_frequency(my_list)
print("Element frequency in my_list:", result)

# 🧠 Explanation:
# The count_frequency function takes a list as input and counts the frequency of each element.
# It uses the Counter class from the collections module to create a frequency distribution.
# The result is returned as a Counter object, which is a subclass of dict.
