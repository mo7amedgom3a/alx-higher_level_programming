#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
print(f"Last digit of {number} is {x}", end=" ")
if (x > 5):
    print("and is greater than 5")
elif (x == 0):
    print("and is 0")
elif (6 > x and x != 0):
    print("and is less than 6 and not 0")
