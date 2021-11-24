import turtle
t = turtle.Turtle()
scrn = turtle.Screen()

def drawE(t, size=100, colour="blue"):
    t.pencolor(colour)
    t.pendown()
    t.forward(size)
    t.backward(size)
    t.left(90)
    t.forward(size*(3/5))
    t.right(90)
    t.forward(size*(7/10))
    t.backward(size*(7/10))
    t.left(90)
    t.forward(size*(3/5))
    t.right(90)
    t.forward(size)

    turtle.penup()
    turtle.setx(turtle.pos()[0]+ size)

if __name__ == "__main__":
    drawE(t)
