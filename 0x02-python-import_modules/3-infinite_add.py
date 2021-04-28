#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    args = sys.argv
    for x in range(1, len(args)):
        result = result + int(args[x])
    print("{:d}".format(result))
