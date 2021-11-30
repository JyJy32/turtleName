import turtle
scrn = turtle.Screen()
bob = turtle.Turtle()


def drawN():
    bob.pensize(1)
    bob.penup()
    bob.forward(30)
    bob.pendown()
    bob.setposition(100, 200)
    bob.rt(60)
    bob.forward(125)
    bob.lt(120)
    bob.forward(125)
    bob.rt(120)
    bob.setposition(300, 0)


if __name__ == "__main__":
    drawN()
    turtle.done()
# Damien
