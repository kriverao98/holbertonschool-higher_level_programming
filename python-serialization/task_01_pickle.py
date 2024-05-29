#!/usr/bin/python3
"""Serialization and Deserialization with Pickle"""
import pickle


class CustomObject:
    """
    A class representing a custom object.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Whether the object is a student or not.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file to save
            the serialized object to.

        Returns:
            None: If serialization is successful.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (IOError, pickle.PickleError) as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.

        Args:
            filename (str): The name of the file to
            deserialize the object from.

        Returns:
            CustomObject: The deserialized object if
            successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject")
                    return None
        except (IOError, pickle.PickleError) as e:
            print(f"Error during deserialization: {e}")
            return None
