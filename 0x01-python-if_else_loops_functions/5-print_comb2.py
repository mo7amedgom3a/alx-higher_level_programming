#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (j == 9 and i != 9):
            print("{:d}{:d}, ".format(i, j), end='')
            i += 1
            continue
        print("{:d}{:d}".format(i, j), end='\n' if i == 9 and j == 9 else ", ")
