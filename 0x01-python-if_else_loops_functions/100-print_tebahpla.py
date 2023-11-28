#!/usr/bin/python3
for n in range(25, -1, -1):
    c = n + ord('A')
    print("{:c}".format(c if n % 2 == 0 else c + 32), end="")
