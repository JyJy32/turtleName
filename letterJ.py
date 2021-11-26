import turtle
t = turtle.Turtle()
scrn = turtle.Screen()


def drawJ(t, size=100, colour="blue"):
    t.penup()
    t.pencolor(colour)
    t.sety(size/2)
    t.right(90)
    t.pendown()
    t.circle(size/2, extent=180)
    t.forward(size)
    t.penup()
    t.right(90)
    t.sety(t.pos()[1]-(1.5*size))

if __name__ == "__main__":
    drawJ(t)
    turtle.done()
