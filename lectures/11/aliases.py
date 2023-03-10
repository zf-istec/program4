#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

print()
opposites = {"up": "down", "right": "wrong", "yes": "no"}

# aliases
alias = opposites

# Shallow copy
copy = opposites.copy()

alias["right"] = "left"
print(opposites["right"])

copy["right"] = "Guiness"
print(opposites["right"])
