#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = []
    for x in my_list:
        if x == search:
            n += [replace]
        else:
            n += [x]
    return n
