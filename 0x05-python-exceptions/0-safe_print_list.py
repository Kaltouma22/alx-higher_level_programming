#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    prnt_elemt = 0

    try:
        for n in range(x):
            print(my_list[n], end='')
            prnt_elemt += 1
    except IndexError:
        pass

    print()
    return prnt_elemt
