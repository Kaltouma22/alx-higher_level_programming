#!/usr/bin/env python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print("")
