#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print()

# this are strings
a = "banana"
b = "banana"

print(a is b)

# but for lists is different
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# advanced stuff
print()
print(id(a))
print(id(b))
print(id(a) == id(b))
print(a is b)
