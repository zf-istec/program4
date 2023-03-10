#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Brad Miller and David Ranum, Learning with Python: Interactive Edition.
"""


def listsum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum


print()
print(listsum([1, 3, 5, 7, 9]))
