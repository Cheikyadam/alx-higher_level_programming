#!/usr/bin/python3
c = 97 + 25
i = 26
while c <= ord('z') and c >= ord('a'):
    d = c
    if i % 2 != 0:
        d = ord(chr(c)) - 32
    print("{}".format(chr(d)), end='')
    c = c - 1
    i = i - 1
