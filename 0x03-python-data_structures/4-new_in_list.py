#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    copy = my_list[:]
    if idx >= 0 and idx <= len(copy) - 1:
        copy[idx] = element
    return copy
