import turtle  # load the turtle module


def drawC(t, size=400):
    scrn = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.setx(t.pos()[0] + size / 2 + size / 40)
    t.pendown()
    t.fd(size / 10)
    t.rt(size / 2.2)
    t.fd(size / 13)
    t.circle(size / 4, extent=180)
    t.fd(size / 10)


if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    scrn = turtle.Screen()
    drawC(t)
    turtle.done()


