import turtle
bob = turtle.Turtle()
scrn = turtle.Screen()

def drawI(t, size=400):
    bob.backward(40)  # move forward 50 pixels
    bob.forward(20)
    bob.left(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(20)
    bob.backward(40)
  
    
    

    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)

if __name__ == "__main__":
    drawI(bob)
    turtle.done()