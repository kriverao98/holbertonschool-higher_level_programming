#!/usr/bin/python3


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    def width(self, value):
        try:
            width += 1
        except TypeError:
            print("width must be an integer")
            
        try:
            width < 0
        except ValueError:
            print("width must be >= 0")
        
    def height(self, value):
        try:
            height += 1
        except TypeError:
            print("width must be an integer")
            
        try:
            height < 0
        except ValueError:
            print("width must be >= 0")
            
    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
        
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        else:
            rectangle_str = ''
            for _ in range(self.height):
                rectangle_str += '#' * self.width + '\n'
            return rectangle_str.rstrip('\n')
