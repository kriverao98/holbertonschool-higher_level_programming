#!/usr/bin/python3
"""Module prints a square."""


def print_square(size):
    """
    Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for a in range(size):
            print("#", end="")
        print()
