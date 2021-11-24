
import turtle


scrn = turtle.Screen()  # Create/obtain the turtle screen object.
bob = turtle.Turtle()
# Create a turtle object, that we can use to draw. (I named it bob for some reason.)


def drawo():

    bob.pensize(1)
    bob.forward(45)  # move forward 50 pixels
    bob.circle(45, 90)
    bob.forward(150)
    bob.circle(45, 90)
    bob.forward(45)
    bob.circle(45, 90)
    bob.forward(150)
    bob.circle(45, 90)
    turtle.done()  # cleanup


drawo()
