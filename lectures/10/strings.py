#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
#### split
song = "The rain in Spain..."
words = song.split()
print(words)

words = song.split("ai")
print(words)

print()
#### join
words = song.split()
glue = ";"
phrase = glue.join(words)
print(phrase)
print(" --- ".join(words))
print("".join(words))
