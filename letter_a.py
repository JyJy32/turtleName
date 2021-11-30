import turtle # load the turtle module

'''
Copy this template for each letter. Then change the functions.
The placeholders in this file just draw rectangles.
'''
def draw_letter_a(turtle, size=400):
    '''Draw lowercase letter.'''
    temppos = turtle.pos()
    turtle.pensize(1)
    turtle.setheading(0)
    turtle.pencolor('grey')
    turtle.penup()
    turtle.forward(size/ 4)
    turtle.left(90)
    turtle.forward(size/ 10)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(size/ 8)
    turtle.penup()
    turtle.right(90)
    turtle.forward(size/10)
    turtle.left(90)
    turtle.circle(size/ 4.44444, 135)# 90
    turtle.pendown()
    turtle.circle(size/ 4.44444, 270)
    turtle.right(135)
    turtle.forward(size/ 15.384615)
    turtle.left(90)
    for side in (size/ 11.11111, size/ 2.22222, size/ 11.11111):
        turtle.forward(side)
        turtle.left(90)
    turtle.forward(size/ 15.384615)
    turtle.penup()
    turtle.setx(temppos[0] + size /2 + size / 40)
    turtle.sety(temppos[1])
    turtle.setheading(0)


    

def draw_capital_letter_a(turtle, size=400):
    '''Draw uppercase letter'''
    draw_letter_a() # change this
