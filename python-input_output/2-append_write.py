#!/usr/bin/python3
"""Appends text to a file and returns the number of characters written."""


def append_write(filename="", text=""):
    """Appends text to a file and returns the number of characters written."""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
