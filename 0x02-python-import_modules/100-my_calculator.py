#!/usr/bin/python3
import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        oper = sys.argv[2]

        if oper == "+":
            result = add(a, b)
        elif oper == "-":
            result = sub(a, b)
        elif oper == "*":
            result = mul(a, b)
        elif oper == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
