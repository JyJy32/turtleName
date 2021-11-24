import turtle
t = turtle.Turtle()
scrn = turtle.Screen()
t.penup()

def drawJ(t=turtle.Turtle(), size=100, colour="blue"):
    t.pencolor(colour)
    t.sety(50)
    t.right(90)
    t.pendown()
    t.circle(size/2, extent=180)
    t.forward(size)

    turtle.penup()
    turtle.setx(turtle.pos()[0]+ size)

if __name__ == "__main__":
    drawJ(t)
