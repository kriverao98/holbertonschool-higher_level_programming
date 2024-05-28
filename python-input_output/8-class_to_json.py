#!/usr/bin/python3
"""Function returns dictionary description"""


def class_to_json(obj):
    """Converts a Python object to a JSON serializable dictionary.

    Args:
        obj (object): The object to be converted.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__