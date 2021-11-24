import turtle
t = turtle.Turtle()
scrn = turtle.Screen()

def drawE(t=turtle.Turtle(), size=100, colour="blue"):
    t.pencolor(colour)
    t.pendown()
    t.forward(size)
    t.backward(size) #_
    t.left(90)
    t.forward(size*(3/5)) #|
    t.right(90)
    t.forward(size*(7/10)) #-
    t.backward(size*(7/10))
    t.left(90)
    t.forward(size*(3/5))#|
    t.right(90)
    t.forward(size)

    t.penup()
    t.sety(turtle.pos()[0]-(size*(3/5)))

if __name__ == "__main__":
    drawE(t)
    turtle.done()
