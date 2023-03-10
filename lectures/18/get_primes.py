#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

David Mertz, Functional Programming in Python
"""

def get_primes():
    """Simple lazy Sieve of Eratosthenes."""
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

primes = get_primes()

print()
print(type(primes))

print(next(primes))
print(next(primes))
print(next(primes))

for _, prime in zip(range(20), primes):
    print(prime, end=" ")

print()
print(next(primes))
