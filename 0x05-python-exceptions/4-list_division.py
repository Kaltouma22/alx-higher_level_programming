#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for n in range(list_length):
            if n >= len(my_list_1) or n >= len(my_list_2):
                print("out of range")
                break
            try:
                result = my_list_1[n] / my_list_2[n]
                result_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result_list.append(0)
    except IndexError:
        print("out of range")
    finally:
        return result_list[:list_length]
