#!/usr/bin/python34
"""Save the given object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Save the given object to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
