#!/usr/bin/python3

import sys as s
if len(s.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(s.argv[1])
except TypeError:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
