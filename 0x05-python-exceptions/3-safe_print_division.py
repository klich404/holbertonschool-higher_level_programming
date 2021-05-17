#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    y = 0.0
    try:
        y = a / b
        x = 1
    except:
        pass
    finally:
        if x == 1:
            print("Inside result: {}".format(y))
            return y
        else:
            print("Inside result: {}".format("None"))
