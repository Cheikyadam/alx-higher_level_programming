#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integ = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                integ += 1
            except (TypeError, ValueError):
                i = i
        print()
    except IndexError:
        print()
        return integ
    else:
        return integ
