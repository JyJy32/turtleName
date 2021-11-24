import turtle # load the turtle module

scrn = turtle.Screen() # Create/obtain the turtle screen object.
bob = turtle.Turtle() # Create a turtle object, that we can use to draw. (I named it bob for some reason.)




def drawG():
    bob.color('green')
    bob.speed(2)
    bob.forward(90) # move forward 50 pixels
    bob.right(90) # turn left 90 degrees
    bob.forward(90)
    bob.circle(-90, 180)
    bob.forward(200)
    bob.circle(-90, 180)

drawG()


turtle.done() # cleanup