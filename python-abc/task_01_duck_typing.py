#!/usr/bin/python3
"""Abstract class that represents a shape"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a shape."""
    
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius):
        """Initialize a Circle object with a given radius."""
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle object with given width and height."""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a given shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle:")
    shape_info(circle)
    print()

    print("Rectangle:")
    shape_info(rectangle)
