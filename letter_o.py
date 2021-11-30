
import turtle


def drawo(t):

    t.pensize(1)
    t.penup()
    t.forward(45)
    t.pendown()
    t.forward(45)
    t.circle(45, 90)
    t.forward(150)
    t.circle(45, 90)
    t.forward(45)
    t.circle(45, 90)
    t.forward(150)
    t.circle(45, 90)


if __name__ == "__main__":
    scrn = turtle.Screen()
    jan = turtle.Turtle()
    drawo(jan)
    turtle.done()
    # jounes
