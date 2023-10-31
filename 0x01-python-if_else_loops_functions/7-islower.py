def islower(c):
    letter = 97
    while letter >= ord('a') and letter <= ord('z'):
        if chr(letter) == c:
            return True
        letter = letter + 1
    return False
