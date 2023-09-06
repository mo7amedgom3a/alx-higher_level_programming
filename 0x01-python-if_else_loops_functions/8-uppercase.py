#!/usr/bin/python3
def uppercase(str):
    for i in str:
        num = ord(i)
        if (num >= 97 and num <= 122):
            num = num - 32
        ch = chr(num)
        print("{:c}".format(ch), end='')
