import turtle

scrn = turtle.Screen()
bob = turtle.Turtle()


def drawS():

    bob.pensize(1)
    bob.penup()
    bob.forward(20)
    bob.pendown()

    bob.forward(40)
    bob.circle(45, 180)
    bob.circle(-45, 180)
    bob.forward(40)
    bob.penup()
    bob.right(90)
    bob.forward(180)


if __name__ == "__main__":
    drawS()
    turtle.done()
