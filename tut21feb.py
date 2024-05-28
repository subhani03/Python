import turtle

def draw_circle(pen):
    pen.setposition(0, -230)
    pen.pendown()
    pen.begin_fill()
    pen.color('yellow')
    pen.pencolor('white')
    pen.circle(200)
    pen.end_fill()
    pen.penup()

def draw_oval(pen):
    pen.color("black")
    pen.pendown()
    pen.begin_fill()
    pen.color('black')
    pen.pencolor('black')
    pen.forward(10)
    for x in range(150):
        pen.right(1)
        pen.forward(0.5)
    pen.forward(30)
    for x in range(150):
        pen.right(1)
        pen.forward(0.5)
    pen.end_fill()
    pen.penup() 

def draw_mouth(pen):
    pen.setposition(-100,-40)
    pen.pendown()
    pen.color('black')
    pen.forward(1)
    for x in range(180):
        pen.right(1)
        pen.backward(1)
    pen.penup()

def draw_u(pen):
    pen.setposition(110,-120)
    pen.pendown()
    pen.begin_fill()
    pen.color('pink')
    pen.backward(1)
    for x in range(130):
        pen.right(1)
        pen.forward(1)
    pen.end_fill()
    pen.up()

win = turtle.Screen()
win.bgcolor('white')
a = turtle.Turtle()
a.speed(10)
a.pensize(10)
a.penup()
#circle(a)
draw_circle(a)
a.speed(10)
a.right(90)
a.setposition(-70,60)
draw_oval(a)
a.speed(0)
a.penup()
a.setposition(150,60)
draw_oval(a)
#u shape
draw_u(a)
a.speed(10)
a.pensize(10)
a.penup()
#mouth
draw_circle(a)
a.speed(10)
a.pensize(10)
a.penup()


turtle.done()




