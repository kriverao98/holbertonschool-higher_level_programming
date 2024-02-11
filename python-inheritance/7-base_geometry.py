#!/usr/bin/python3
"""This class represents a base geometry."""


class BaseGeometry:
    """This class represents a base geometry."""
    def area(self):
        """Raises an exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the given value is an integer and greater than 0."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
