#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lis = []
    convert = 0.0
    x = 0
    for i in range(0, list_length):
        convert = 0
        try:
            convert = my_list_1[i] / my_list_2[i]
            x = 1
        except TypeError:
            print("wrong type")
            lis += [0]
        except ZeroDivisionError:
            print("division by 0")
            lis += [0]
        except IndexError:
            print("out of range")
            lis += [0]
        finally:
            if x == 1:
                x = 0
                lis += [convert]
    return(lis)
