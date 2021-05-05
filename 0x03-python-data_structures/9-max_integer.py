#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        n = my_list[0]
        for x in my_list:
            if n < x:
                n = x
        return n
