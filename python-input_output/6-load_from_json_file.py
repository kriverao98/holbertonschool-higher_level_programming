#!/usr/bin/python3
"""Loads data from json file"""
import json


def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The data loaded from the JSON file.

    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
