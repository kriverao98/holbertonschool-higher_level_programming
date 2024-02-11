#!/usr/bin/python3
"""Read and print the content of a file."""


def read_file(filename=""):
    """Read and print the content of a file."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
