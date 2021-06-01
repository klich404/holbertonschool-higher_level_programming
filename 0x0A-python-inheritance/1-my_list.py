#!/usr/bin/python3
"""
    a class MyList
    that inherits
    from list
"""


class MyList(list):
    """
    my Mylist class
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
