#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted((list(a_dictionary)))
    for key in sort:
        print("{:s}: {}".format(key, a_dictionary[key]))
