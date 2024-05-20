#!/usr/bin/python3
"""This function replaces '.', '?', and ':' for 2 new lines"""


def text_indentation(text):
    """
    Add indentation to the given text by inserting two newlines after each occurrence of '.', '?', or ':'.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the input text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
        print(text, end="")
