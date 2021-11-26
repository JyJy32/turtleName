def drawJ(t, size=100, colour="blue"):
    t.penup()
    t.pencolor(colour)
    t.sety(size*0.25)
    t.right(90)
    t.pendown()
    t.circle(size*0.25, extent=180)
    t.forward(size*0.75)
    t.penup()
    t.right(90)
    t.sety(t.pos()[1]-size)

if __name__ == "__main__":
    import turtle
    t = turtle.Turtle()
    scrn = turtle.Screen()
    drawJ(t)
    turtle.done()
