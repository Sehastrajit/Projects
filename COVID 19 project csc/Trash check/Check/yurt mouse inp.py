import turtle as tim
import random

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.set_heading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

colors = ["red", "blue", "green", "yellow", "black"]

def clickLeft(x, y):  # Make sure to have parameters x, y
    tim.color(random.choice(colors))

def clickRight(x, y):
    tim.stamp()

tim.listen()

tim.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
tim.onscreenclick(clickRight, 3) # 3: Right Mouse Button

tim.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
tim.onkey(down, "Down")
tim.onkey(left, "Left")
tim.onkey(right, "Right")

tim.mainloop() 
