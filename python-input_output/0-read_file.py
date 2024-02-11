#!/usr/bin/python3
"""Read and print the contents of a file."""


def read_file(filename=""):
    """Read and print the contents of a file."""
    with open(filename, "r") as file:
        content = file.read()
        print(content)
