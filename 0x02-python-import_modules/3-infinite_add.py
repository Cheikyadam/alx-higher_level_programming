#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    sum = 0
    for i in range(1, leng):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
