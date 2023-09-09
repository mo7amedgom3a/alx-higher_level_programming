#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    lis = reversed(my_list)
    for i in lis:
        print("{:d}".format(i))
