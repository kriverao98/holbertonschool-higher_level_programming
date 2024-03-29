#!/usr/bin/python3
"""Module creates a class named Square"""


class Square:
    """This module creates a class Square"""

    def __init__(self, size=0):
        """Initializes the data"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
