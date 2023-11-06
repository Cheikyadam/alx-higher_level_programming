#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list.insert(idx, element)
    my_list.remove(my_list[idx + 1])
    return my_list
