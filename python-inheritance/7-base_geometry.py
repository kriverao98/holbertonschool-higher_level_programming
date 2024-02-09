#!/usr/bin/python3


class BaseGeometry:
    """This class represents a base geometry with an area method and an integer validator."""
    def area(self):
        """Raises an exception indicating that the area() method is not implemented."""

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates if the given value is an integer and greater than 0."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
