#!/usr/bin/python3
"""
    function that adds 2 integers

    protoype: add_integer(a, b=98)
"""


def add_integer(a, b=98):
    """
    add 2 integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
