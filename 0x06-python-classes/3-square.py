#!/usr/bin/python3
"""
This class defines a squeare.
"""


class Square:
    """A Squeare with size and area"""

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        a = self.__size * self.__size
        return(a)
