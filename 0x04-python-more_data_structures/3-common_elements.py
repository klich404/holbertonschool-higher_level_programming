#!/usr/bin/python3
def common_elements(set_1, set_2):
    l = []
    for x in set_1:
        if (x not in l) and (x in set_2):
            l.append(x)
    return l
