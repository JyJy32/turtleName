
import turtle


def drawU(t, size=100, colour="blue"):

    t.pensize(1)
    t.penup()
    t.forward(size*0.50)
    t.pendown()
    t.forward(size*0.125)
    t.circle(45, 90)
    t.forward(size*1.4)
    t.penup()
    t.left(90)
    t.forward(size*1)
    t.left(90)
    t.pendown()
    t.forward(size*1.4)

    t.circle(45, 90)

    t.penup()
    t.forward(size*0.80)
    t.pendown()


if __name__ == "__main__":
    scrn = turtle.Screen()
    jan = turtle.Turtle()
    drawU(jan)
    turtle.done()
    # jounes
