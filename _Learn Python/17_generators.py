# 📘 Program: Using Generators in Python
# This program demonstrates how to define and use a generator using the yield keyword

'''
  Generators are a special type of iterable that allow you to iterate over a sequence of values without storing them all in memory at once.
  They are defined using the yield keyword, which allows the function to return a value and pause its execution, resuming later from where it left off.
  Generators can be used to iterate over a sequence of values without storing the entire sequence in memory.
'''

# Defining a generator function to yield numbers from 1 to n
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Pauses and returns the current value
        count += 1

# Using the generator
for num in count_up_to(5):
    print("Generated:", num)

# 🧠 Explanation:
# Unlike return, yield pauses the function and resumes later.
# count_up_to(5) creates a generator object that produces numbers 1 to 5 one by one.
