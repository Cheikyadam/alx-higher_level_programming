#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:]
    new_list.insert(idx, element)
    new_list.remove(my_list[idx])
    return new_list
