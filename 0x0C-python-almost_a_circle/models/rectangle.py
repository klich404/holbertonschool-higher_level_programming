#!/usr/bin/python3
"""
A Rectangle class who can:
Assign each argument width, height, x and y to the right attribute.
Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
Returns the area value of the Rectangle instance.
Prints in stdout the Rectangle instance with the character #.
Returns the dictionary representation of a Rectangle.
Assigns a key/value argument to attributes.

"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Assign each argument width, height, x and y to the right attribute
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        i = self.id
        w = self.__width
        h =self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        if self.__width != 0 and self.__height != 0:
            for a in range(self.__y):
                print()

            for i in range(self.__height):
                for b in range(self.__x):
                    print(" ", end="")
                for x in range(self.__width):
                    print("#", end="")
                print()
        else:
            print()

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle
        """
        i = self.id
        w = self.__width
        h =self.__height
        x = self.__x
        y = self.__y
        return {'x': x, 'y': y, 'id': i, 'height': h, 'width': w}

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
                if n == 2:
                    self.height = arg
                if n == 3:
                    self.x = arg
                if n == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
