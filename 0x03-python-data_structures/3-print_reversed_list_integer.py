#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    leng = len(my_list)
    if leng != 0:
        leng = leng - 1
        for i in range(leng, -1, -1):
            print("{:d}".format(my_list[i]))