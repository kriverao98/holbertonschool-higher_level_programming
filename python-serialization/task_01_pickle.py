#!/usr/bin/python3
"""Class that serializes and deserializes using pickle"""
import pickle


class CustomObject:
    """
    A class representing a custom object.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates whether the object is a student or not.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Indicates whether the
            object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the CustomObject instance and saves it to a file.

        Args:
            filename (str): The name of the file
            to save the serialized object to.

        Returns:
            None
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
        Deserializes a CustomObject instance from a file.

        Args:
            filename (str): The name of the file to
            deserialize the object from.

        Returns:
            CustomObject or None: The deserialized CustomObject
            instance, or None if an error occurred.
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
