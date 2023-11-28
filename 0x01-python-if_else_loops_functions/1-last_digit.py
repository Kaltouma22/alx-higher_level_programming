#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = number % 10 if number > 0 else number % -10
print(f"Last digit of {number} is {ldigit}"
      ,end=" ")
if ldigit > 5:
    print("and is greater than 5")
elif ldigit == 0:
    print("and is 0")
else:
    print(f"and is less than 6 and not 0")
