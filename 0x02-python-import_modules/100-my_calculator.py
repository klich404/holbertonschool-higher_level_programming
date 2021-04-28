#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        s = ['+', '-', '*', '/']
        x = 0
        for y in s:
            if args[2] == y:
                x = 1
                break
        if x == 0:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = args[1]
            b = args[3]
            if args[2] == s[0]:
                print("{:s} + {:s} = {:d}".format(a, b, add(int(a), int(b))))
            elif args[2] == s[1]:
                print("{:s} - {:s} = {:d}".format(a, b, sub(int(a), int(b))))
            elif args[2] == s[2]:
                print("{:s} * {:s} = {:d}".format(a, b, mul(int(a), int(b))))
            elif args[2] == s[3]:
                print("{:s} / {:s} = {:d}".format(a, b, div(int(a), int(b))))
