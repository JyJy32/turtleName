import turtle
t = turtle.Turtle()
scrn = turtle.Screen()

def drawL(t, size=10):
    t.color('red')
    t.pendown()
    t.forward(85)
    t.backward(85)
    t.left(90)
    t.forward(175)
  
    
    

    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)

if __name__ == "__main__":
    drawE(t)
    turtle.done()