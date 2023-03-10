#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Brad Miller and David Ranum, Learning with Python: Interactive Edition.
"""


def listsum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listsum(num_list[1:])


print()
print(listsum([1, 3, 5, 7, 9]))
#print(listsum([]))
