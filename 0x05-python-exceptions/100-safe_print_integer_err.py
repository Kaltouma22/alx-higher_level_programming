#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        print()
        return True
    except ValueError as e:
        print("Exception:", e, file=sys.stderr)
        return False
