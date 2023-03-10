#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# first without composition
response = input("What is your radius? ")
r = float(response)
area = 3.14159 * r**2
print("The area is", area)

# now let's use composition
r = float( input("What is your radius? ") )
print("The area is", 3.14159 * r**2)

# All in one statement
print("The area is", 3.14159*float(input("What is your radius? " ))**2)
