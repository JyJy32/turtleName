
import turtle


def drawU(bob):

    bob.pensize(1)
    bob.penup()
    bob.left(90)
    bob.forward(150)
    bob.right(180)
    bob.pendown()
    bob.forward(150)
    bob.circle(45, 90)
    bob.forward(50)
    bob.circle(45, 90)
    bob.forward(150)
    bob.penup()
    bob.right(180)
    bob.forward(190)
    bob.left(90)


if __name__ == "__main__":
    scrn = turtle.Screen()
    bob = turtle.Turtle()
    drawU(bob)
    turtle.done()
