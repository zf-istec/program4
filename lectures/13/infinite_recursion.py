# -*- coding: utf-8 -*-
"""

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def recursion_depth(number):
    print("{0}, ".format(number), end="")
    recursion_depth(number + 1)

recursion_depth(0)
