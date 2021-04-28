#!/usr/bin/python3
if __name__ = "__main_-":
    import sys
    args = sys.argv
    if len(args) == 1:
        print("{} arguments.".format(len(args) - 1))
    elif len(args) == 2:
        print("{} argument:".format(len(args) - 1))
    else:
        print("{} arguments:".format(len(args) - 1))
        for x in range(len(args)):
            if x != 0:
                print("{:d}: {}".format(x, args[x]))
