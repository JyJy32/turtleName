import turtle


def drawP(schild, size=300, colour="blue"):
    startx, starty = schild.pos()
    schild.pencolor(colour)
    schild.left(90)
    schild.forward(size)  # move forward 50 pixels
    schild.right(90)  # turn left 90 degrees
    schild.forward(90)
    schild.circle(-66, extent=90, steps=5)
    schild.circle(-66, extent=90, steps=5)
    schild.forward(90)
    schild.right(90)
    schild.penup()
    schild.setx(schild.pos()[0] + size/2)
    schild.sety(starty)
    schild.right(90)


if __name__ == "__main__":
    scrn = turtle.Screen()
    schild = turtle.Turtle()
    drawP(schild)
