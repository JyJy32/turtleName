import turtle

scrn = turtle.Screen()
bob = turtle.Turtle()


def drawS():

    bob.pensize(1)
    bob.penup()
    bob.setpos(50, 80)
    bob.pendown()

    bob.forward(40)
    bob.backward(40)
    bob.circle(-45, -90)
    bob.circle(-45, -95)
    bob.circle(45, -185)
    bob.backward(40)


if __name__ == "__main__":
    drawS()
    turtle.done()
