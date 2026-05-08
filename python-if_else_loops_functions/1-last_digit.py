#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

if number > 0:
    remainder = number % 10
else:
    remainder = -(( -1 * number ) % 10)

if remainder > 5:
    compare = "and is greater than 5"
elif remainder == 0:
    compare = "and is 0"
elif remainder < 6:
    compare = "and is less than 6 and not 0"

print(f"Last digit of {number} is {remainder} {compare}")
