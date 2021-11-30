
import turtle


def drawU(bob, size=100):

    bob.pensize(1)
    bob.penup()
    bob.left(90)
    bob.forward(1.5*size)
    bob.right(1.8*size)
    bob.pendown()
    bob.forward(1.5*size)
    bob.circle(0.45*size, 90)
    bob.forward(0.5*size)
    bob.circle(0.45*size, 90)
    bob.forward(1.5*size)
    bob.penup()
    bob.right(180)
    bob.forward(1.9*size)
    bob.left(90)
    bob.forward(0.1*size)


if __name__ == "__main__":
    scrn = turtle.Screen()
    bob = turtle.Turtle()
    drawU(bob)
    turtle.done()
