#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

def scompar(word):
    if word < "banana":
        return "Your word, " + word + ", comes before banana."
    elif word > "banana":
        return "Your word, " + word + ", comes after banana."
    else:
        return "Yes, we have bananas!"


print()
print(scompar("ananas"))
print(scompar("banana"))
print(scompar("port"))
