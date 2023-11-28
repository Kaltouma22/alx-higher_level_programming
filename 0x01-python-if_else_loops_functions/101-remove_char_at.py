#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join([c for i, c in enumerate(s) if i != n])
