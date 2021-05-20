#!/usr/bin/python3
"""This class defines a rectangle"""


class Rectangle:
    """A Rectangle with width, height, area and perimeter"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        s = ""
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    s += ("#")
                if i != self.__height - 1:
                    s += '\n'
            return s
