#!/usr/bin/python3
def weight_average(my_list=[]):
    leng = len(my_list)
    if leng == 0:
        return 0
    score = 0
    som = 0
    for tup in my_list:
        score = score + tup[0] * tup[1]
        som = som + tup[-1]
    return score / som
