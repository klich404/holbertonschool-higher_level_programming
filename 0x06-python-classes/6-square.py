#!/usr/bin/python3
"""This class defines a squeare"""


class Square:
    """A Squeare with size and area"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        for z in position:
            if type(z) is not int or z < 0 or len(position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        for z in self.__position:
            if type(z) is not int or z < 0 or len(self.__position) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")

    def area(self):
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        if self.__size == 0:
            for a in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for b in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
