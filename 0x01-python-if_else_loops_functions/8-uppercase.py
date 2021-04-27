#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            letter = ord(str[x]) - 32
        else:
            letter = ord(str[x])
        print("{:c}".format(letter), end="")
    print()
