import turtle
def draw_circle(pen):
    pen.pendown()
    pen.setposition(0,-70)
    pen.color('yellow')
    pen.pencolor('yellow')
    pen.begin_fill()
    pen.circle(150)
    pen.end_fill()
    pen.penup()

def draw_eyebrow(pen):
    pen.pendown()
    pen.setposition(-20,120)
    pen.color('black')
    pen.pencolor('black')
    pen.forward(1)
    for x in range(40):
        pen.right(1)
        pen.forward(1)
    pen.penup()
    


def draw_eye(pen):
    pen.pendown()
    pen.color('black')
    pen.pencolor('black')
    pen.begin_fill()
    pen.forward(1)
    for x in range(40):
        pen.left(1)
        pen.backward(1)
    for x in range(40):
        pen.right(1)
        pen.forward(1)
    pen.penup()

def draw_mouth(pen):
    pen.pendown()
    pen.color('black')
    pen.begin_fill()
    pen.pencolor('black')
    pen.circle(40,40)
    pen.penup()
    

win=turtle.Screen()
win.bgcolor('white')
a=turtle.Turtle()
a.speed(0)
a.pensize(8)
a.penup()
#circle
draw_circle(a)
a.speed(0)
a.penup()
#eyebrow
draw_eyebrow(a)
a.speed(0)
a.right(90)
a.penup()

#eye
a.speed(0)
a.goto(-10,70)
a.right(90)
a.penup()

#mouth

a.speed(0)
a.goto(-20,-20)
a.penup()


turtle.done()