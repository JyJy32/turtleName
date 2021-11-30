def drawE(t, size=400, colour="blue"):
    t.pencolor(colour)
    t.pendown()
    t.forward(size/2)
    t.backward(size/2) #_
    t.left(90)
    t.forward(size/2) #|
    t.right(90)
    t.forward(size*(2/7)) #-
    t.backward(size*(2/7))
    t.left(90)
    t.forward(size/2)#|
    t.right(90)
    t.forward(size/2)
    t.penup()

    t.sety(t.pos()[1]-size)


if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    scrn = turtle.Screen()
    drawE(t)
    turtle.done()
