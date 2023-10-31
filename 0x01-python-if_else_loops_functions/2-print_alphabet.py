#!/usr/bin/python3
c = 97
while c >= ord('a') and c <= ord('z'):
    print("{}".format(chr(c)), end='')
    c = c + 1
