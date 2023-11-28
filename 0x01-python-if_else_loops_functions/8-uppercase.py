#!/usr/bin/env python3
def uppercase(str):
    for c in s:
        print("{:c}"
              .format(ord(c) - 32) if 'a' <= c <= 'z' else c
              , end="")
        print()
