#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = [False] * len(my_list)
    for count, i in enumerate(my_list):
        if (i % 2 == 0):
            newlist[count] = True
    return newlist
