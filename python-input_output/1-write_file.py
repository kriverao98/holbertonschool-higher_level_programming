#!/usr/bin/python3
"""Writes the given text to the specified file."""


def write_file(filename="", text=""):
    """Writes the given text to the specified file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
