#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if len(args) == 0:
            Result = fct()
        else:
            Result = fct(args[0], args[1])
    except (ValueError) as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return None
    except IndexError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return None
    except TypeError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return None
    except ZeroDivisionError as ze:
        sys.stderr.write("Exception: {}\n".format(ze))
        return None
    else:
        return Result
