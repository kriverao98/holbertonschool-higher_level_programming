#!/usr/bin/python3
"""A class representing a student."""


class Student:
    """A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the student object to a JSON representation.

        Args:
            attrs (list, optional): A list of attributes to include
            in the JSON representation.
                If None, all attributes are included.

        Returns:
            dict: A dictionary representing the student object in JSON format.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
