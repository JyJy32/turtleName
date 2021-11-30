import turtle


scrn = turtle.Screen() # Create/obtain the turtle screen object.
bob = turtle.Turtle() # Create a turtle object, that we can use to draw. (I named it bob for some reason.)
def drawM(bob, size=100):
    bob.color("pink")
    bob.left(75)
    bob.forward(100)
    bob.right(150)
    bob.forward(90)
    bob.left(150)
    bob.forward(90)
    bob.right(150)
    bob.forward(100)
    turtle.done()

if __name__ == "__main__":
    drawM()
