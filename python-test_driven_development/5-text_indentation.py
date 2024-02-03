#!/usr/bin/python3
"""module prints 2 newline after char .,?,:"""


def text_indentation(text):
    """function prints 2 newline after char .,?,:"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            new_text += "\n\n"

    print(new_text.strip())
