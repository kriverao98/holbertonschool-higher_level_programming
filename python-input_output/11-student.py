#!/usr/bin/python3
"""A module containing a class representing a student."""


class Student:
    """A class representing a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object to a JSON representation.

        Args:
            attrs (list): A list of attributes to include in
            the JSON representation.

        Returns:
            dict: A dictionary representing the Student object in JSON format.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Reload the Student object from a JSON representation.

        Args:
            json (dict): A dictionary representing the
            Student object in JSON format.
        """
        for key, value in json.items():
            setattr(self, key, value)
