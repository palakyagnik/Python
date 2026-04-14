#Write a program to create abstract class with one method.

from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Derived Class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Main Program
r = Rectangle(5, 3)

print("Area of Rectangle:", r.area())
