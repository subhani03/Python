
import turtle

def draw_circle(pen):
    pen.setpos(0,0)
    pen.pendown()
    pen.begin_fill()
    pen.color('red')
    pen.pencolor('red')
    pen.circle(100)
    pen.end_fill()
    pen.penup()

def draw_eye(pen):
    pen.color('black')
    pen.pencolor('black')
    pen.pendown()
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()
    pen.up()

def draw_eyebrow(pen):
    pen.color('black')
    pen.pencolor('black')
    pen.goto(-15,120)
    pen.begin_fill()
    pen.down()
    pen.backward(1)
    for x in range(100):
        pen.left(0.7)
        pen.backward(0.5)
    for x in range(100):
        pen.right(0.7)
        pen.forward(0.5)
    pen.end_fill()
    pen.up()

def draw_eyebrowr(pen):
    pen.color('black')
    pen.pencolor('black')
    pen.goto(10,120)
    pen.begin_fill()
    pen.down()
    pen.forward(1)
    for x in range(100):
        pen.right(0.5)
        pen.backward(0.5)
    for x in range(100):
        pen.left(0.7)
        pen.forward(0.5)
    pen.end_fill()
    pen.up()
    
def draw_mouth(pen):
    pen.color('black')
    pen.pencolor('black')
    pen.goto(-50,150)
    pen.down()
    pen.forward(1)
    for x in range(100):
        pen.right(1)
        pen.backward(1)
    
    pen.up()
    
win = turtle.Screen()
win.bgcolor('white')
a = turtle.Turtle()
a.speed(0)
a.pensize(8)
a.penup()
#circle
draw_circle(a)
a.speed(0)
a.right(90)
#eye
a.speed(0)
a.setposition(-35,120)
draw_eye(a)
a.speed(0)
a.setposition(35,120)
a.penup()
draw_eye(a)
#eyebrow
draw_eyebrow(a)
a.speed(0)
a.penup()
draw_eyebrowr(a)
a.speed(0)
a.penup()
#mouth
draw_mouth(a)
a.speed(0)
a.penup()


turtle.done()