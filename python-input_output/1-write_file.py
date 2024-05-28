#!/usr/bin/python3
"""This function returns the number of characters in a txt file"""


def write_file(filename="", text=""):
    """Return char number in txt file"""
    with open(filename, 'w', encoding="utf-8") as file:
        char_num = file.write(text)
    return char_num
