#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to a file.

    Args:
        data: The data to be serialized.
        filename: The name of the file to save the serialized data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a file.

    Args:
        filename: The name of the file to load the data from.

    Returns:
        The deserialized data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
