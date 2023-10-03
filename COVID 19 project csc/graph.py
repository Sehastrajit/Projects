import turtle
turtle.clearscreen()


def drawBar(t, height):
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 



xs = [7.47*(10**6), 7.63*(10**6),7.87*(10**6), 8.049*(10**6), 8.24*(10**6)] 
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()            
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

t = turtle.Turtle()           
t.color("blue")
t.fillcolor("red")
t.pensize(3)

import turtle
t2=turtle.Turtle()

t2.hideturtle()

t2.penup()
t2.setposition(0,0)
t2.showturtle()
t2.pendown()
t2.forward(280)





for a in xs:
    drawBar(t, a)

