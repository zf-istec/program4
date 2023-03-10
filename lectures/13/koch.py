# -*- coding: utf-8 -*-
"""

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def koch(pen, order, size):
    """
    Make turtle pen draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """
    if order == 0:
        # The base case is just a straight line
        pen.forward(size)
    else:
        koch(pen, order-1, size/3)  # recursive call
        pen.left(60)  # Go 1/3 of the way
        koch(pen, order-1, size/3)  # recursive call
        pen.right(120)
        koch(pen, order-1, size/3)  # recursive call
        pen.left(60)
        koch(pen, order-1, size/3)  # recursive call

# a better version
#def koch(pen, order, size):
#    if order == 0:
#        pen.forward(size)
#    else:
#        for angle in [60, -120, 60, 0]:
#            koch(pen, order-1, size/3)  # recursive call
#            pen.left(angle)

# get a pen
import turtle

canvas = turtle.Screen()
canvas.setup(800, 300)
canvas.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pencolor("blue")
tess.shape("circle")
tess.shapesize(0.1)

tess.penup()
tess.goto(-300, -100)
tess.pendown()

koch(tess, 0, 600)
#koch(tess, 1, 600)
#koch(tess, 2, 600)
#koch(tess, 3, 600)
#koch(tess, 4, 600)

canvas.mainloop()     # Wait for user to close window
turtle.bye()
#wn.exitonclick()      # wait for a user click on the canvas
