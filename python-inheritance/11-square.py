#!/usr/bin/python3


class Square(__import__('9-rectangle').Rectangle):
    """ Square inherits from Rectangle """

    def __init__(self, size):
        """ Constructor """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""
        return super().area()
