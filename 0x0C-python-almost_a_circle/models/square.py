#!/usr/bin/python3
"""
A Squeare class who can:
Call the super class with id, x, y, width and height.
Return [Square] (<id>) <x>/<y> - <size>.
Returns the dictionary representation of a Rectangle.
Assigns a key/value argument to attributes.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Call the super class with id, x, y, width and height
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return [Square] (<id>) <x>/<y> - <size>
        """
        i = self.id
        s = super().width
        x = super().x
        y = super().y
        return "[Square] ({}) {}/{} - {}".format(i, x, y, s)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        i = self.id
        s = super().width
        x = super().x
        y = super().y
        return {'id': i, 'x': x, 'size': s, 'y': y}

    def update(self, *args, **kwargs):
        """
        Assigns a key/value argument to attributes
        """
        if len(args) > 0:
            for n, arg in enumerate(args):
                if n == 0:
                    self.id = arg
                if n == 1:
                    self.width = arg
                    self.height = arg
                if n == 2:
                    self.x = arg
                if n == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
