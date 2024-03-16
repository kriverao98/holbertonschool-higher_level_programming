#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Return size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
        
    def __update(self, id=None, size=None, x=None, y=None):
        """Update the attributes of the Rectangle object."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    
    def update(self, *args, **kwargs):
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)
        
    def to_dictionary(self):
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
def __update(self, id=None, size=None, x=None, y=None):
    """Update the attributes of the Square object."""
    if id is not None:
        self.id = id
    if size is not None:
        self.size = size
        self.width = size
        self.height = size
    if x is not None:
        self.x = x
    if y is not None:
        self.y = y
