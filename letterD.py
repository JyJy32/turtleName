import turtle  # load the turtle module



def draw(bob, size=400):
    bob.pendown()
    bob.setheading(90)
    bob.forward(size)
    bob.right(90)
    bob.circle(-size/2, 180)
    bob.penup()
    bob.setx(turtle.pos()[0] + size / 10)


if __name__ == "__main__":
    
    scrn = turtle.Screen()  # Create/obtain the turtle screen object.
    jan = turtle.Turtle()  # Create a turtle object, that we can use to draw.
    draw(jan)
