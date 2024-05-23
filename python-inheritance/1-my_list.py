#!/usr/bin/python3
"""A class that inherits from list and prints a sorted list"""


class MyList(list):
    """This class inherits from list"""
    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
