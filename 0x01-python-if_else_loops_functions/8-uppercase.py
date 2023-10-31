def uppercase(str):
    letter = 97
    for c in str:
        while letter >= ord('a') and letter <= ord('z'):
            if chr(letter) == c:
                c = chr(ord(c) - 32)
            letter = letter + 1
        print("{}".format(c), end='')
        letter = 97
    print("{}".format(""))
