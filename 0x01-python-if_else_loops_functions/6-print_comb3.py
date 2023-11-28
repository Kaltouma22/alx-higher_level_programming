#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        print("{:d}{:d}, ".format(tens, ones), end="")
print("{:d}{:d}".format(9, 9))
