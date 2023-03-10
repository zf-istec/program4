#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


A = {1, 2, 3}
B = {3, 2, 3, 1}

print(A == B)  # True
print(B)       # {1, 2, 3}

print(id(A) == id(B))  # False

A = set([1, 2, 3])
B = set([3, 2, 3, 1])

print(A == B)  # True
print(B)       # {1, 2, 3}
