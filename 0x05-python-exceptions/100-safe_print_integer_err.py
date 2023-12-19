#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    a_num = True

    try:
        frmt_val = "{:d}".format(int(value))
        print(frmt_val)
    except ValueError as e:
        print("Exception:", e, file=sys.stderr)
        a_num = False
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        a_num = False
    return a_num
