#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError):
        Result = None
    else:
        Result = result
    finally:
        print("Inside result: {}".format(Result))
        return Result
