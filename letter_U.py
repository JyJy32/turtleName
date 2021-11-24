
import turtle


scrn = turtle.Screen()
bob = turtle.Turtle()


def drawU():

    bob.pensize(1)
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.forward(45)
    bob.circle(45, 90)
    bob.forward(150)
    bob.backward(150)
    bob.circle(45, -90)
    bob.backward(45)
    bob.circle(45, -90)
    bob.backward(150)


if __name__ == "__main__":
    drawU()
    turtle.done()
