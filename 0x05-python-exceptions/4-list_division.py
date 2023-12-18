#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for n in range(list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except (ZeroDivisionError, IndexError, TypeError) as e:
            if isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, TypeError):
                print("wrong type")
            else:
                print("out of range")
            result = 0
        finally:
            res_list.append(result)
    return res_list
