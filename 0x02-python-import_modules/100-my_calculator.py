#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    oper = sys.argv[2]
    b = int(sys.argv[3])

    if oper == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif oper == "-":
        print(f"{a} - {b} = {sub(a, b)}")
    elif oper == "*":
        print(f"{a} * {b} = {mul(a, b)}")
    elif oper == "/":
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
