import math
# Shape Class
# Main Class/Base Class
class Shape:
    # Method
    def area(self): # Not defining constructor just defining method.
        pass
# Subclass 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
# Subclass 3
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length**2
# Subclass 4
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 1/2
Shape1 = Circle(7)
print(Shape1.area())
Shape2 = Rectangle(4, 5)
print(Shape2.area())
Shape3 = Square(9)
print(Shape3.area())
Shape4 = Triangle(6, 5)
print(Shape4.area())
