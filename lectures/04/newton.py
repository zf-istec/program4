#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers, 
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

n = int(input("input number n: "))
threshold = 0.001      # use more precision if needed

approximation = n/2    # Start with some or other guess at the answer

while True:
    better = (approximation + n/approximation)/2
    #print(better)
    if abs(approximation - better) < threshold:
        print("approx root: ", better)
        break
    approximation = better
