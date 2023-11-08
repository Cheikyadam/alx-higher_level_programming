#!/usr/bin/python3
def search_replace(my_list, search, replace):
    leng = len(my_list)
    new_list = []
    if leng != 0:
        for i in range(leng):
            a = my_list[i]
            if a == search:
                a = replace
            new_list.append(a)
    return new_list
