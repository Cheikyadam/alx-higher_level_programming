#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    if leng == 1:
        print("0 arguments.")
    else:
        if leng == 2:
            print("{:d} argument:".format(leng - 1))
        else:
            print("{:d} arguments:".format(leng - 1))
        for i in range(1, leng):
            print("{:d}: {}".format(i, sys.argv[i]))
