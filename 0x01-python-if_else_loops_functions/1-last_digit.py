#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {}".format(number)
if number < 0:
    n = abs(number) % 10
    if n == 0:
        x = "is {}".format(n)
    else:
        x = "is -{}".format(n)
    n = n * -1
else:
    n = abs(number) % 10
    x = "is {:d}".format(n)
if n > 5:
    print("{} {} and is greater than 5".format(str, x))
elif n == 0:
    print("{} {} and is 0".format(str, x))
elif n < 6:
    print("{} {} and is less than 6 and not 0".format(str, x))
