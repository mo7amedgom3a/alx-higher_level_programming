#!/usr/bin/python3
from sys import argv
size = len(argv) - 1

if (size == 0):
    print("{} arguments.".format(size))
else:
    arg = argv[1:]
    print("{} arguments:".format(size))
    for i in range (size):
        print("{}: {}".format(i + 1, arg[i]))