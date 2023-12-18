#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print(int(value))
        print()
        return True
    except (ValueError, TypeError):
        return False
