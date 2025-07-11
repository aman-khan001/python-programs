# 📘 Program: Inheritance in Python (OOP)
# This program demonstrates how a child class inherits from a parent class


'''
 Inheritance is a fundamental concept in OOP that allows a class (child class) to inherit attributes and methods from another class (parent class).
'''

# Defining the parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Defining the child class that inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Creating objects of both classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling the speak method
animal.speak()  # Output: Generic Animal makes a sound.
dog.speak()     # Output: Buddy barks.

# 🧠 Explanation:
# Dog class inherits from Animal. It overrides the speak() method.
# The child class can use methods and properties of the parent class unless overridden.
# This allows for code reuse and extension of functionality.

