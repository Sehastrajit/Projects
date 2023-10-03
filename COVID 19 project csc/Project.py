
#imports
import time
import countrystat
import deathstat
import winsound ,time,turtle

stat=open("status.txt")
status=stat.read()

def signout():
        turtle.penup()
        turtle.clear()
        turtle.hideturtle()
        turtle.bgcolor("black")
        
        turtle.color('white')
        style = ('Courier',40, 'italic')

        turtle.setposition(0,100)
        turtle.write('Successfully ', font=style, align='center')
        turtle.setposition(0,50)
        turtle.write('signed out', font=style, align='center')
        time.sleep(3)
        startule()
def choose():
        c1=input("Choose an option to view table based on the option=")
        turtle.clear()
        if c1=="death" or c1=="Death":
                deathstat.deathstat()
                options()
        elif c1=="Total" or c1=="total" :
                allstat.allstat()
                turtle.clearscreen()
                options()
        elif c1=="country" or c1=="Country" :
                countrystat.countrystat()
                options()
        elif c1=="infected" or c1=="Infected":
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
        turtle.setposition(150,-100)
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
        turtle.color('white')
        style = ('Courier',40, 'italic')

        turtle.setposition(0,100)
        turtle.write('Choose an option to view table based on the option', font=style, align='center')

        style = ('Courier',20, 'italic')
        turtle.setposition(0,50)
        turtle.write('Total', font=style, align='center')

        turtle.setposition(0,0)
        turtle.write('Country', font=style, align='center')

        turtle.setposition(0,-50)
        turtle.write('Death', font=style, align='center')


        turtle.setposition(0,-100)
        turtle.write('Infected', font=style, align='center')


        turtle.setposition(0,-150)
        turtle.write('Signout', font=style, align='center')

        choose()




def loading():
        import turtle
        turtle.penup()
        turtle.setposition(20, 200)
        turtle.clearscreen()
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
        sgc="cyan"


#Login SCREEN

def loginscr():
        turtle.clear()
        style = ('Courier',70, 'italic')
        turtle.setposition(-100,150)
        turtle.write('Login', font=style, align='center')

        style = ('Courier',20, 'italic')
        turtle.setposition(-50,0)
        turtle.write('User name=', font=style, align='center')

        turtle.setposition(-50,-100)
        turtle.write('Password=', font=style, align='center')

def signupscr():
        turtle.clear()
        style = ('Courier',70, 'italic')
        turtle.setposition(-100,150)
        turtle.write('Sign-up', font=style, align='center')

        style = ('Courier',20, 'italic')
        turtle.setposition(-50,0)
        turtle.write('Username=', font=style, align='center')

        turtle.setposition(-50,-100)
        turtle.write('Password=', font=style, align='center')

        turtle.setposition(-50,-200)
        turtle.write('Re-Enter Password=', font=style, align='center')


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
            turtle.setposition(150,0)
            turtle.write(username, font=style, align='center')


            password=input("Password= ")
          
            if password==d[j]:
                if username=="admin":
                        admin.admin()
                        login()
                else:
                        Start.statuscheck()
                        mview()
            else:
                print("Incorrect password")
                style = ('Courier',20, 'italic')
                turtle.setposition(150,-100)
                turtle.write("*"*len(password), font=style, align='center')

                style = ('Courier',10, 'italic')
                turtle.setposition(150,-130)
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
        print("\n"*3)
        print("signup")
        print("^^^^^^^")
        global newpass,repass,newuser
        turtle.color('white')
        
        newuser=input("Username=")
        
        style = ('Courier',20, 'italic')
        turtle.setposition(150,0)
        turtle.write(newuser, font=style, align='center')
        
        
        newpass=input("Choose Password=")

        style = ('Courier',20, 'italic')
        turtle.setposition(150,-100)
        turtle.write("*"*len(newpass), font=style, align='center')



        
        repass=input("Re-enter Password=")

        style = ('Courier',20, 'italic')
        turtle.setposition(150,-200)
        turtle.write("*"*len(repass), font=style, align='center')
    signupdetails()
    if newpass==repass:
        d[newuser]=newpass
        print("account suceefully created")
        login()
    else:
        turtle.color('orange red')
        turtle.setposition(50,-250)
        style = ('Courier',10, 'italic')
        turtle.write("*passwords don't match", font=style, align='center')
        turtle.color('white')

        time.sleep(2)
        signup()






#sound
#winsound.PlaySound("Sound512.wav",winsound.SND_ASYNC)

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

time.sleep(6)

#Starting turtle screen

def startule():
        turtle.clear()

        time.sleep(2)
        sgc="black"

        turtle.bgcolor(sgc)
        turtle.color('indigo')
        turtle.hideturtle()
        turtle.penup()

        style = ('Courier',40, 'italic')
        turtle.setposition(-100,190)
        turtle.write('COVID 19 Data \n  and \n   Staticts', font=style, align='center')

        style = ('Courier',30, 'italic')
        turtle.setposition(0,90)
        turtle.write('Main Menu', font=style, align='center')

        turtle.color('white')
        style = ('Courier',20, 'italic')
        turtle.setposition(0,0)
        turtle.write('Login', font=style, align='center')

        turtle.setposition(0,-100)
        turtle.write('Signup', font=style, align='center')

        turtle.setposition(0,-200)
        turtle.write('Exit', font=style, align='center')
        
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

startule()


