#!/usr/bin/python3
def multiple_returns(sentence):
    str = sentence
    if str == "":
        return len(str), None
    return len(str), str[0]
