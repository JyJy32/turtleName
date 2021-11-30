import turtle  # load the turtle module


def draw(t, size=400):
    t.penup()
    t.setx(t.pos()[0] + size / 2 + size / 40)
    t.sety(size / 2)
    t.pendown()
    t.fd(size / 10)
    t.rt(size / 2.2)
    t.fd(size / 13)
    t.circle(size / 4, extent=180)
    t.fd(size / 10)
    t.penup()
    t.setx(size)
    t.sety(size / 2)


if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    scrn = turtle.Screen()
    draw(t)
    turtle.done()


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
