#!/usr/bin/env python3
def uppercase(str):
    for u in s:
        print("{:c}"
              .format(ord(u) if not islower(u) else ord(u) - 32),
              end="")
    print("")

def islower(u):
    if (ord(u) >= ord('a') and ord(u) <= ord('z')):
        return True
    else:
        return False
