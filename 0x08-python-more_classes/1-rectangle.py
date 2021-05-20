#!/usr/bin/python3
"""This class defines a rectangle"""

class Rectangle:
    """A Rectangle with width and height"""
    pass


def __init__(self, width=0, height=0):
    self.__width = width
    self.__heaight = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = width
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = height
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
