import turtle

scrn = turtle.Screen()  # Create/obtain the turtle screen object.
# Create a turtle object, that we can use to draw. (I named it bob for some reason.)
bob = turtle.Turtle()


def drawP(t, size=100, colour="blue"):

    bob.left(90)
    bob.forward(100)  # move forward 50 pixels
    bob.right(90)  # turn left 90 degrees
    bob.forward(30)
    bob.circle(-22, extent=90, steps=5)
    bob.circle(-22, extent=90, steps=5)
    bob.forward(30)
    bob.right(90)
    turtle.penup()
    turtle.setx(turtle.pos()[0] + size)


if __name__ == "__main__":
    drawP(bob)
