#!/usr/bin/python3
"""Saves an update list using function 5 and 6"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    # Load existing data from file
    data = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, initialize an empty list
    data = []

# Add arguments to the list
data.extend(args)

# Save the updated list to the file
save_to_json_file(data, filename)
