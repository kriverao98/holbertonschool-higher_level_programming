#!/usr/bin/python3
"""
    This function returns the JSON representation of an obj

    Returns:
        json.dumps(my_obj): obj(str) to return
"""
import json


def to_json_string(my_obj):
    """Returns OBJ"""
    return json.dumps(my_obj)
