#!/usr/bin/python3
"""This is the base class for geometry operations."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string represention of Rectangle object """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
