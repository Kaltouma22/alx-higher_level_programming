#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    prnt_ntg = 0
    elmt_prnt = 0

    try:
        while elmt_prnt < x:
            val = my_list[elmt_prnt]
            if (isinstance(val, int)):
                print("{:d}".format(val), end='')
                prnt_ntg += 1
            elmt_prnt += 1
    except IndexError:
        pass

    print()
    return prnt_ntg
