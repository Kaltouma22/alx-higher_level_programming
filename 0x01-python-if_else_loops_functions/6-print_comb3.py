#!/usr/bin/python3
for tens in range(9):
    for ones in range(tens + 1, 10):
        if (tens == 8 and ones == 9):
            print("89")
        else:
            print("{:d}{:d}, ".format(tens, ones), end="")
