        
#imports

import time
import countrystat
import deathstat
import time,turtle

stat=open("status.txt")
status=stat.read()


def signout():
        turtle.penup()
        turtle.clear()
        turtle.hideturtle()
        style = ('Courier',40, 'italic')
        turtle.bgcolor("black")
        turtle.bgpic("signed.gif")
        turtle.setposition(200,-230)
        turtle.write('.', font=style, align='center')
        time.sleep(3)
        startule()


def choose():
        c1=input("Choose an option to view table based on the option=")
        turtle.clearscreen()
        if c1=="death" or c1=="Death":
                turtle.bgpic("dead.gif")
                turtle.bgcolor("black")
                deathstat.deathstat()
                options()
        elif c1=="Total" or c1=="total" :
                turtle.bgpic("fight.gif")
                turtle.bgcolor("black")
                allstat.allstat()
                turtle.clearscreen()
                options()
        elif c1=="country" or c1=="Country" :
                turtle.bgpic("total.gif")
                turtle.bgcolor("black")
                countrystat.countrystat()
                options()
        elif c1=="infected" or c1=="Infected":
                turtle.bgpic("infe.gif")
                turtle.bgcolor("black")
                infectstat.infectstat()
                options()
        elif c1=="Signout" or c1=="signout":
                signout()

        else:
                print("Wrong input")
                options()
                

import countrystat
import deathstat
import infectstat
import allstat
import admin
import Start

def mview():
        print("\n"*20)
        style = ('Courier',20, 'italic')
        turtle.setposition(50,0)
        turtle.write("*"*len(password), font=style, align='center')

        time.sleep(3)
        loading()

        turtle.penup()
        turtle.hideturtle()
        turtle.bgcolor("orange red")
        turtle.color('black')
        style = ('Courier',70, 'italic')
        turtle.setposition(-50,0)
        turtle.write(' Welcome Back', font=style, align='center')

        
        print("Welcome Back",username)
        time.sleep(5)
        options()
        
def options():
        turtle.penup()
        turtle.clear()
        turtle.hideturtle()
        turtle.bgcolor("black")
        turtle.bgpic("options.gif")
        turtle.setposition(200,-230)
        turtle.write('.', font=style, align='center')
        print('''Contions for viewing table
                        Country

                        Death

                        Infected
                        
                        Total
                        
                        Signout''')
        choose()




def loading():
        import turtle
        turtle.clearscreen()
        turtle.penup()
        turtle.setposition(20, 100)
        turtle.bgcolor("orange red")
        turtle.bgpic("loadin.gif")
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
        sgc="cyan"


#Login SCREEN

def loginscr():
        turtle.clearscreen()
        turtle.penup()
        style = ('Courier',40, 'italic')
        turtle.bgcolor("black")
        turtle.bgpic("login.gif")

def signupscr():
        turtle.clearscreen()
        turtle.penup()
        turtle.bgcolor("black")
        turtle.bgpic("signup.gif")

#START SCREEN
        

                
def startup():
    print('''Covid19 Database and Graphs
                Menu

                Login

                Signup

                Exit''')
    ask=input("Login/Signup/Exit=")    
    if ask=="Login" or ask=="login":
        login()
    elif ask=="Signup" or ask=="signup":
        signup()
    elif ask=='Exit'or'exit':
        print("Thank You")
        turtle.bgpic("tq.gif")
        turtle.bgcolor("black")
        time.sleep(4)
        turtle.bgpic("sayin1.gif")
        turtle.bgcolor("black")
        time.sleep(4)
        exit()
    else:
        print("wrong input")
        startup()

    
#LOGIN

def login():
    turtle.penup()
    loginscr()
    turtle.color("white")
    turtle.hideturtle()
    print("\n"*3)
    print("Login")

    print("^^^^^^")
    a=open("D:\\COVID 19 project csc\\20.csv")
    c=a.readlines()
    global password,username
    username=input("Username= ")
    for j in d:
        if j==username:

            style = ('Courier',20, 'italic')
            turtle.setposition(50,110)
            turtle.write(username, font=style, align='center')


            password=input("Password= ")
          
            if password==d[j]:
                if username=="admin":
                        style = ('Courier',20, 'italic')
                        turtle.setposition(50,0)
                        turtle.write("*"*len(password), font=style, align='center')
                        admin.admin()
                        login()
                else:
                        Start.statuscheck()
                        mview()
            else:
                print("Incorrect password")
                style = ('Courier',20, 'italic')
                turtle.setposition(50,0)
                turtle.write("*"*len(password), font=style, align='center')

                turtle.color("red")
                style = ('Courier',20, 'italic')
                turtle.setposition(110,-60)
                turtle.write("*Incorrect Password", font=style, align='center')


                time.sleep(2)

                turtle.clear()
                loginscr()
                login()

    else:
        print("usernasme not found")
        login()

#SIGNUP

def signup():
    def signupdetails():
        signupscr()
        turtle.hideturtle()
        print("\n"*3)
        print("signup")
        print("^^^^^^^")
        global newpass,repass,newuser
        turtle.color('black')
        
        newuser=input("Username=")
        
        style = ('Courier',20, 'italic')
        turtle.setposition(100,30)
        turtle.write(newuser, font=style, align='center')
        
        
        newpass=input("Choose Password=")

        style = ('Courier',20, 'italic')
        turtle.setposition(100,-70)
        turtle.write("*"*len(newpass), font=style, align='center')



        
        repass=input("Re-enter Password=")

        style = ('Courier',20, 'italic')
        turtle.setposition(100,-186)
        turtle.write("*"*len(repass), font=style, align='center')
    signupdetails()
    if newpass==repass:
        d[newuser]=newpass
        print("account suceefully created")
        time.sleep(6)
        login()
    else:
        turtle.color('orange red')
        turtle.setposition(150,-230)
        style = ('Courier',20, 'italic')
        turtle.write("*passwords don't match", font=style, align='center')
        turtle.color('white')

        time.sleep(2)
        signup()






#view adjustment
time.sleep(3)

screen = turtle.Screen()

  #set size:

screen.setup(width = 0.9, height = 0.75)


turtle.bgcolor("orange red")
turtle.color('black')
style = ('Courier',40, 'italic')
turtle.write('Press windows key + left arrow', font=style, align='center')
turtle.hideturtle()

time.sleep(10)


#Starting turtle screen

def startule():
        turtle.bgcolor("black")
        turtle.bgpic("menu.gif")
        turtle.clear()

        time.sleep(2)
        turtle.hideturtle()

        time.sleep(0.3)

        startup()

a=open("D:\\COVID 19 project csc\\202.txt")

c=a.readlines()

d = {}
for i in range(0,len(c)):
    x=c[i]
    (key, val)= x.split(":")
    d[key]= val.rstrip("\n")
turtle.clear()
turtle.bgcolor("black")
turtle.bgpic("corona.gif")
turtle.penup()
turtle.setposition(200,-230)
turtle.write('.', font=style, align='center')
time.sleep(10)


startule()




