""" import turtle
win = turtle.Screen()
win.bgcolor('black')
pen = turtle.Turtle()
pen.speed(10)
pen.pensize(10)
pen.penup()
pen.setposition(0, -280)
pen.pendown()
pen.begin_fill()
pen.color('red')
pen.pencolor('white')
pen.circle(300)
pen.end_fill()
pen.penup() """
#inner circle
""" import turtle
s=turtle.Turtle()

s.setposition(0, -230)

s.pendown()
s.begin_fill()
s.color('black')
s.circle(250)
s.end_fill()
s.penup()
 """
 


""" import turtle

pen = turtle.Turtle()
pen.speed(10)
pen.pensize(10)
pen.penup()
pen.setposition(0, -280)
pen.pendown()
pen.pensize(2)
pen.setposition(0, -230)
pen.pendown()
pen.begin_fill()
pen.color('red')
pen.circle(250)
pen.end_fill()
pen.penup()
turtle.done() """
#triangle
import turtle
pen=turtle.Turtle()
pen.pensize(10)
pen.setposition(53, -40)
pen.pendown()
pen.begin_fill()
pen.color('black')
pen.pencolor('white')
pen.right(90)
pen.forward(100)
pen.right(115)
pen.forward(250)
pen.right(157)
pen.forward(227)
pen.end_fill()