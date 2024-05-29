#!/usr/bin/python3
"""Convert data from CSV to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if the conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
