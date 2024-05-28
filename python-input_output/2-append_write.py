#!/usr/bin/python3
"""Append string to end of txt file"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        char_num = file.write(text)
    return char_num
