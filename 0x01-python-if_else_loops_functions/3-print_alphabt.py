#!/usr/bin/python3
c = 97
while c >= ord('a') and c <= ord('z'):
    if chr(c) not in "eq":
        print("{}".format(chr(c)), end='')
    c = c + 1
