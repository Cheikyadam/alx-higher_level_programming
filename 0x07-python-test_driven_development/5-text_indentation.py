#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for c in text.strip():
        if i == 1 and c == ' ':
            i = 0
            continue
        print(c, end='')
        i = 0
        if c == '.' or c == '?' or c == ':':
            i = 1
            print()
