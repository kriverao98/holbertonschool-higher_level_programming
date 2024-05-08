#!/usr/bin/python3
import random
number = random.randint(-10, 10)
"""
This function generates a random number
between -10 and 10 and prints whether
the number is positive, negative, or zero.
"""

if number > 0:
    print(f"{number} is positive")

elif number == 0:
    print(f"{number} is zero")

else:
    print(f"{number} is negative")
