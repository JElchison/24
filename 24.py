#!/usr/bin/env python3

import itertools
import sys


numbers = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
symbols = ['+', '-', '*', '/']
target = 24


def evaluate(permutation):
    (num1, num2, num3, num4), sym1, sym2, sym3 = permutation

    expressions = [
        "((%d %s   %d) %s  %d)  %s %d  ",
        " (%d %s  (%d  %s  %d)) %s %d  ",
        " (%d %s   %d) %s (%d   %s %d) ",
        "  %d %s ((%d  %s  %d)  %s %d) ",
        "  %d %s  (%d  %s (%d   %s %d))"
    ]
    for expression in expressions:
        string = expression % (num1, sym1, num2, sym2, num3, sym3, num4)
        try:
            result = eval(string)
            if result == target:
                print("%s = %s" % (string, target))
        except ZeroDivisionError:
            pass


for permutation in itertools.product([i for i in itertools.permutations([3, 3, 7, 8])], symbols, symbols, symbols):
    evaluate(permutation)
