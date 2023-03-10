#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def factorialR(n):
    """Recursive factorial function with a assert."""
    assert isinstance(n, int) and n >= 1
    return 1 if n <= 1 else n * factorialR(n-1)

print()
print(factorialR(5))
print(factorialR(0))
print(factorialR('a'))
