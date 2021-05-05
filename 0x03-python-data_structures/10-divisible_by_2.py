#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    l = []
    for x in my_list:
        if x % 2 == 0:
            l.append(True)
        else:
            l.append(False)
    return l
