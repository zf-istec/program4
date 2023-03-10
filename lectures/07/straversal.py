# -*- coding: utf-8 -*-
"""
Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

word = "Banana"

for letter in word:
    print(letter)

print()

# a very BAD way
ix = 0
while ix < len(word):
    letter = word[ix]
    print(letter)
    ix += 1
