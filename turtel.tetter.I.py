import turtle 
import turtle  # load the turtle module

scrn = turtle.Screen()  # Create/obtain the turtle screen object.
# Create a turtle object, that we can use to draw. (I named it bob for some reason.)
bob = turtle.Turtle()


bob.backward(40)  # move forward 50 pixels
bob.forward(20)
bob.left(90)
bob.forward(100)
bob.right(90)
bob.forward(20)
bob.backward(40)

turtle.done()  # cleanup

