#!/usr/bin/python3
"""Base class for geometry operations"""


class BaseGeometry:
    """This class raises an exception if area is empty"""
    def area(self):
        raise Exception("area() is not implemented")
