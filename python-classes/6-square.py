#!/usr/bin/python3
"""This class defines square"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Print a visual representation of the square.

        If the size is 0, it prints an empty line.
        Otherwise, it prints a square made of '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
