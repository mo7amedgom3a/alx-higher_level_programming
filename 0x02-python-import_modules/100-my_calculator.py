#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div

    from sys import exit, argv
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
    }

    size = len(argv) - 1
    if (size != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if (op not in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    res = ops[op](a, b)
    print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))
