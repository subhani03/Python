import turtle
def draw_circle(pen):
    pen.setposition(0,-120)
    pen.pendown()
    pen.begin_fill()
    pen.color('yellow')
    pen.pencolor('yellow')
    pen.circle(150)
    pen.end_fill()
    pen.penup()
def draw_eye(pen):
    pen.pendown()
    pen.color('black')
    pen.begin_fill()
    pen.pencolor('black')
    pen.circle(10)
    pen.end_fill()
    pen.penup()
def draw_mouth(pen):
    pen.pendown()
    pen.color('black')
    pen.pencolor('black')
    pen.forward(1)
    for x in range(180):
        pen.right(1)
        pen.forward(1)
    pen.penup()

win=turtle.Screen()
win.bgcolor('white')
a=turtle.Turtle()
a.speed(0)
a.pensize(5)
a.penup()
#circle
draw_circle(a)
a.speed(0)
a.penup()
#eye
a.speed(0)
a.setposition(-50,50)
a.penup()
draw_eye(a)
a.speed(0)
a.setposition(50,50)
draw_eye(a)
a.penup()
#mouth
a.setposition(60,-10)
a.speed(0)
a.right(90)
draw_mouth(a)
a.penup()



turtle.done()