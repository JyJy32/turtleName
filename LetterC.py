import turtle  # load the turtle module


def draw():
    scrn = turtle.Screen()

    bob = turtle.Turtle()
    bob.fd(40)
    bob.rt(180)
    bob.fd(30)
    bob.circle(100, extent=180)
    bob.fd(40)


# def draw(turtle, size=400):
#     '''Draw lowercase letter.'''
#     turtle.pensize(1)
#     turtle.setheading(0)
#     turtle.pencolor('grey')
#     turtle.pendown()
#     for s in (1, 2):
#         for side in (size / 2, size):
#             turtle.forward(100)
#             turtle.left(90)
#     turtle.penup()
#     turtle.setx(turtle.pos()[0] + size / 2 + size / 40)
