# 📘 Program: Object-Oriented Programming (OOP) Basics
# This program demonstrates basic concepts of classes and objects in Python


'''
  Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods.
  Objects are instances of classes, which can contain both data (attributes) and functions (methods).
  Classes define the structure and behavior of objects.

  OOP allows for encapsulation, inheritance, and polymorphism, making code more modular and reusable.

  In this example, we define a simple class named Person with attributes for name and age, and a method to greet.
  
  '''

# Defining a class named Person
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects of the Person class
person1 = Person("John", 25)
person2 = Person("Max", 22)

# Calling the greet method
person1.greet()  # Output: Hello, my name is Aman and I am 25 years old.
person2.greet()  # Output: Hello, my name is Kiran and I am 22 years old.

# 🧠 Explanation:
# The __init__ method initializes the object when it's created.
# self refers to the instance of the class. Methods can access attributes using self.
# You can create multiple instances of the class, each with its own attributes.


