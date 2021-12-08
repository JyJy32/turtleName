import turtle # load the turtle module
import time

'''
Copy this template for each letter. Then change the functions.
The placeholders in this file just draw rectangles.
'''
def draw_letter_k(turtle, size=400):
    '''Draw lowercase letter.'''
    temppos = turtle.pos()
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('blue')
    turtle.pendown()
    turtle.forward(size/ 12)
    turtle.left(90)
    turtle.forward(size/ 4)
    turtle.right(60)
    turtle.forward(size / 10)
    turtle.right(90)
    turtle.forward(size / 2.89)
    turtle.left(60)
    turtle.forward(size / 10)
    turtle.left(120)
    turtle.forward(size / 2.539)
    turtle.right(90)
    turtle.forward(size / 5)
    turtle.left(90)
    turtle.forward(size / 10)
    turtle.left(90)
    turtle.forward(size / 3)
    turtle.right(120)
    turtle.forward(size / 2.2)
    turtle.left(90)
    turtle.forward(size / 12.3)
    turtle.left(90)
    turtle.sety(temppos[1])
    turtle.penup()
    turtle.setx(temppos[0] + size /2 + size / 40)
    turtle.setheading(0)

    

def draw_capital_letter_k(turtle, size=400):
    '''Draw uppercase letter'''
    draw_letter_k() # change this
