#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as c
    import sys as s
    if len(s.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(s.argv[1])
    b = int(s.argv[3])
    op = s.argv[2]
    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if op == '+':
        print("{:d} + {:d} = {:d}".format(a, b, c.add(a, b)))
    elif op == '-':
        print("{:d} - {:d} = {:d}".format(a, b, c.sub(a, b)))
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, c.mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, c.div(a, b)))
