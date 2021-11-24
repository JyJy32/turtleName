
import turtle


scrn = turtle.Screen()
bob = turtle.Turtle()


def drawo():

    bob.pensize(1)
    bob.penup()
    bob.forward(45)
    bob.pendown()
    bob.forward(45)
    bob.circle(45, 90)
    bob.forward(150)
    bob.circle(45, 90)
    bob.forward(45)
    bob.circle(45, 90)
    bob.forward(150)
    bob.circle(45, 90)
    turtle.done()  # cleanup


if __name__ == "__main__":
    drawo()
    turtle.done()
