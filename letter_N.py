import turtle
scrn = turtle.Screen()
bob = turtle.Turtle()


def drawN():
    bob.pensize(1)
    bob.penup()
    bob.forward(30)
    bob.pendown()
    bob.left(90)
    bob.forward(150)
    bob.right(150)
    bob.forward(175)
    bob.left(150)
    bob.forward(155)


if __name__ == "__main__":
    drawN()
    turtle.done()
