#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self, value):
        try:
            width += 1
        except TypeError:
            print("width must be an integer")

        try:
            width < 0
        except ValueError:
            print("width must be >= 0")

    def height(self, value):
        try:
            height += 1
        except TypeError:
            print("width must be an integer")

        try:
            height < 0
        except ValueError:
            print("width must be >= 0")

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
