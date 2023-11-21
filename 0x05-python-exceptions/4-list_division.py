#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = list()
    try:
        for i in range(0, list_length):
            c = 1
            try:
                a = my_list_1[i]
            except IndexError:
                c = 0
                print("out of range")
            try:
                b = my_list_2[i]
            except IndexError:
                c = 0
                print("out of range")
            if c == 0:
                new.append(0)
            else:
                try:
                    result = a / b
                    new.append(result)
                except (ZeroDivisionError):
                    new.append(0)
                    print("division by 0")
                except TypeError:
                    print("wrong type")
                    new.append(0)
    finally:
        return new
