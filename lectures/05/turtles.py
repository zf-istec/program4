#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code adapted from the book:

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""

import turtle


def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")

alex = turtle.Turtle()      # Create alex
draw_square(alex, 50)       # Call the function to draw the square

alex.penup()
alex.goto(100, 100)
alex.pendown()

draw_square(alex, 75)        # Draw another square

wn.mainloop()
turtle.bye()

