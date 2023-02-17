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
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.check_type(value, "width")
        self.__width = value
            
    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.check_type(value, "height")
        self.__height = value
            
    @property
    def x(self):
        """Return the x-coordinate of the rectangle."""
        return self.__x
        
    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        self.check_type(value, "x")
        self.__x = value
            
    @property
    def y(self):
        """Return the y-coordinate of the rectangle."""
        return self.__y
        
    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        self.check_type(value, "y")
        self.__y = value
            
    def check_type(self, value, name, eq=True):
            """Check if the value is of the correct type and raise an error if not."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        
    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height
