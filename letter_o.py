
import turtle


def drawo(t, size=100, colour="blue"):

    t.pensize(1)
    t.penup()
    t.forward(size*0.50)
    t.pendown()
    t.forward(size*0.25)
    t.circle(45, 90)
    t.forward(size*1)
    t.circle(45, 90)
    t.forward(size*0.25)
    t.circle(45, 90)
    t.forward(size*1)
    t.circle(45, 90)

    t.penup()
    t.forward(size*0.80)
    t.pendown()


if __name__ == "__main__":
    scrn = turtle.Screen()
    jan = turtle.Turtle()
    drawo(jan)
    turtle.done()
    # jounes
