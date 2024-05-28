
""" import turtle
s=turtle.Turtle()
s.pensize(10)
s.circle(100)
s.seth(15)
s.circle(100)
turtle.done() 
 """
""" import turtle
s=turtle.Turtle()
s.forward(100)
s.backward(50)
s.right(90)
s.dot()
s.forward(100)
s.home()
s.goto(60,60)
s.shape("circle")
s.left(750)
turtle.done() """

""" import turtle
t=turtle.Turtle()
t.speed(1)
t.penup()
t.setpos(-20,40)
t.pendown()
t.pensize(10)
t.pencolor("pink")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()             """     

import turtle
colors = [ "pink","yellow","blue","green","white","red"]
sketch = turtle.Pen()
sketch.speed(0)
turtle.bgcolor("black")
for i in range(100):
   sketch.pencolor(colors[i % 6])
   sketch.width(i/100 + 1)
   sketch.forward(i)
   sketch.left(59)  
turtle.done() 

