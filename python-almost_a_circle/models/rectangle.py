#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """Represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width 
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_type(value, "width")
        self.__width = value
            
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_type(value, "height")
        self.__height = value
            
    @property
    def x(self):
        return self.__x
        
    @x.setter
    def x(self, value):
        self.check_type(value, "x")
        self.__x = value
            
    @property
    def y(self):
        return self.__y
        
    @y.setter
    def y(self, value):
        self.check_type(value, "y")
        self.__y = value
            
    def check_type(self, value, name):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
