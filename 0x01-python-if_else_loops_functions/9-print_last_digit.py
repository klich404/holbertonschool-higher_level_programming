#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number)
    print("{}".format(n % 10), end="")
    return n % 10
