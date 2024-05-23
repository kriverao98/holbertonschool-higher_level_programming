#!/usr/bin/python3
"""Check given value"""


class BaseGeometry:
    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks given value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
