#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operations = {
        "+":
        "-":
        "*":
        "/":
    }

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    oper = sys.argv[2]
    if oper not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {oper} {b} = {operations[oper](a, b)}")
