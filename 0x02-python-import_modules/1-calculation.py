#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    added = add(a, b)
    subt = sub(a, b)
    mult = mul(a, b)
    divide = div(a, b)
    print("{} + {} = {}".format(a, b, added))
    print("{} - {} = {}".format(a, b, subt))
    print("{} * {} = {}".format(a, b, mult))
    print("{} / {} = {}".format(a, b, divide))

