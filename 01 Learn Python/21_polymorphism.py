# 🐥 Program: Polymorphism in Python (OOP)


'''
  Polymorphism is a core concept in Object-Oriented Programming (OOP) that allows methods to do different things based on the object it is acting upon.
'''

# Defining a parent class
class Shape:
    def area(self):
        print("This shape has no area formula defined.")

# Defining a subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Defining a subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Using polymorphism
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())

# 🧠 Explanation:
# Each subclass has its own version of the area() method.
# Polymorphism allows us to use the same method name with different implementations.
# This is achieved through method overriding.
# The for loop iterates over a list of different shape objects, calling the area() method on each.
# This demonstrates how polymorphism allows for flexible and reusable code.
