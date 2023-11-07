#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        first = None
    else:
        first = sentence[0]
    return (leng, first)
