import turtle

#------------------------------------------------------------------------------
# Make some shapes
#   Work through exercises 1-4 in Chapter 4.3.
#------------------------------------------------------------------------------

# Square
# NOTE: for part 2 of 4.3, you will add another parameter to this function

def square(t, length):
    """
    Draw a square using Turtle t

    >>> don = turtle.Turtle()
    >>> square(don, 200)
    """

    t.fd(length)
    t.rt(90)
    t.fd(length)
    t.rt(90)
    t.fd(length)
    t.rt(90)
    t.fd(length)

    turtle.mainloop()


## Polygon

def polygon(t, n, length):
    """
    Draw a polygon using Turtle t

    >>> don = turtle.Turtle()
    >>> polygon(don, 7, 200)
    """

    for i in range(n):
        t.fd(length)
        t.rt(360/n)

    turtle.mainloop()


## Circle

def circle(t, r):
    """
    Draw a circle using Turtle t

    >>> don = turtle.Turtle()
    >>> circle(don, 50)
    """

    for i in range(150):
        t.fd((r*3.1415926*2)/150)
        t.rt(360/150)

    turtle.mainloop()

# john = turtle.Turtle()
# square(john,100)
# polygon(john,7,100)
# circle(john,10) # This file calls all three functions with these lines uncommented, but because of some Tkinter error that I think is outside the scope of this RJ (_tkinter.TclError: invalid command name ".!canvas"), it only runs one of these three lines before the program quits.

#------------------------------------------------------------------------------
# Make some art
#   Complete *at least one of* Exercise 2, 3, 4, or 5 in `shapes.py`.
#------------------------------------------------------------------------------

# If you come up with some cool drawings you'd like to share with the rest of the class, let us know!

def hyperbolic_spiral(t, lines):
    """
    Draw a hyperbolic spiral using Turtle t

    >>> don = turtle.Turtle()
    >>> hyperbolic_spiral(don, 360)
    """

    for i in range(lines):
        t.fd(1)
        t.lt(lines/(i+1))

    turtle.mainloop()


# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
#    doctest.run_docstring_examples(square, globals(), verbose=True)
