import turtle


def drawN(t):

    t.pensize(1)
    t.penup()
    t.forward(30)
    t.pendown()
    t.left(90)
    t.forward(150)
    t.right(150)
    t.forward(175)
    t.left(150)
    t.forward(155)


if __name__ == "__main__":
    scrn = turtle.Screen()
    jan = turtle.Turtle()
    drawN(jan)
    turtle.done()

    # jounes
