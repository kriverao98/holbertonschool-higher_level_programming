#!/usr/bin/python3
"""Load a JSON file and return the deserialized object."""
import json


def load_from_json_file(filename):
    """Load a JSON file and return the deserialized object."""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
