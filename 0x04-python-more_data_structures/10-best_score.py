#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    my_keys = list(a_dictionary)
    best_key = ''
    best = a_dictionary[my_keys[0]]
    for k, v in a_dictionary.items():
        if v >= best:
            best_key = k
    return best_key
