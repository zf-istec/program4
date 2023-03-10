#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def find_first_2_letter_word(words):
    for word in words:
        if len(word) == 2:
            return word
    return ""


print(find_first_2_letter_word(["This", "is", "a", "dead", "parrot"]))

print(find_first_2_letter_word(["I", "like", "cheese"]))
