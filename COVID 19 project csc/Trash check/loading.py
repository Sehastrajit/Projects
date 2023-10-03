def loading():
        import turtle
        turtle.penup()
        turtle.setposition(40, 100)
        turtle.clear()
        turtle.bgcolor("orange red")
        turtle.color('black')
        style = ('Courier',30, 'italic')
        turtle.write('Loading...', font=style, align='right')
        turtle.hideturtle()


        #loading screen movements
        c = 1
        a = turtle.Turtle()
        b = turtle.Turtle()
        c = turtle.Turtle()
        d = turtle.Turtle()
        a.pensize(5)
        a.penup()
        b.pensize(5)
        b.penup()
        c.pensize(5)
        d.pensize(10)
        d.hideturtle()
        d.penup()
        d.goto(-50, -20)
        d.pendown()

        a.forward(50)
        a.left(90)
        a.forward(50)
        a.left(90)
        a.pendown()
        b.forward(50)
        b.left(90)
        b.pendown()
        for x in range(50):
                a.forward(50)
                a.left(90)
                b.forward(50)
                b.left(90)
                c.forward(50)
                c.left(90)
                d.forward(3)


        time.sleep(0.5)
        turtle.clearscreen()

        #steting game bg color
        sgc="cyan"
        turtle.bgcolor(sgc)
