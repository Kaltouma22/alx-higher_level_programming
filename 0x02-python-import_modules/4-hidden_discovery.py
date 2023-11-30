#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for h in dir(hidden_4):
        if not h.startswith("__"):
            print(h)
