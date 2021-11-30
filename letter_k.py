import turtle # load the turtle module
import time

'''
Copy this template for each letter. Then change the functions.
The placeholders in this file just draw rectangles.
'''
def draw_letter_k(turtle, size=400):
    '''Draw lowercase letter.'''
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('grey')
    turtle.pendown()
    for s in (1, 2):
        for side in (size / 2, size):
            turtle.forward(side)
            turtle.left(90)
 


    temppos = turtle.pos()
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('blue')
    turtle.forward(size/ 10)
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
    # for side in (size/ 11.11111, size/ 2.22222, size/ 11.11111):
    #     turtle.forward(side)
    #     turtle.left(90)
    # turtle.forward(size/ 15.384615)
    # turtle.penup()
    # turtle.setx(temppos[0] + size /2 + size / 40)
    # turtle.sety(temppos[1])


    

def draw_capital_letter_k(turtle, size=400):
    '''Draw uppercase letter'''
    draw_letter_k() # change this

draw_letter_k(turtle, 400)
time.sleep(2) 