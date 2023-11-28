#!/usr/bin/python3
for lower in range(ord('a'), ord('z') + 1):
    if (lower != ord('q') and lower != ord('e')):
        print("{:c}".format(lower), end="")
