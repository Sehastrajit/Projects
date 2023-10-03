#admin
import turtle,time
def mview1():
        time.sleep(3)

        turtle.penup()
        turtle.hideturtle()
        turtle.bgcolor("orange red")
        turtle.color('black')
        style = ('Courier',70, 'italic')
        turtle.setposition(-50,0)
        turtle.write(' Welcome Back', font=style, align='center')

        
        print("Welcome Back member")
        time.sleep(5)
        options()

def update():
    import sqlite3 as sqlite
    import turtle , time
    print("Instruction: Enter the query")
    print()
    query=input("Enter the query= ")
    con = sqlite.connect('covid191.db')
    cur = con.cursor()
    
    a=cur.execute(query)
    z=cur.fetchall()

    print()
    t=int(input("Type 0 to end view table"))

    time.sleep(t)

    con.commit()
    con.close()
    achoice()

def server():
    stat=open("status.txt",'w')
    status=input("Activate/Deactivate")
    if status=="Activate" or status=="activate":
        stat.write("Activate")
    elif status=="Deactivate" or status=="deactivate":
        stat.write("Deactivate")
    else:
        print("Wrong input")
        print()
        server()
def achoice():
    print("\n"*2)
    print("Server/Update/Mview/Squit")
    print()
    adchoice=input("Choose the operation to perform=")
    if adchoice=="Server" or adchoice=="server":
        server()
    elif adchoice=="Update" or adchoice=="update":
        update()
    elif adchoice=="Mview" or adchoice=="mview":
        import trash1.loading
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
        trash1.loading()
        achoice()
    else:
        print("Wrong Input")
        achoice()

def admin():
    turtle.clearscreen()
    turtle.penup()
    turtle.bgcolor("black")
    turtle.bgpic("admin.gif")
    style = ('Courier',40, 'italic')
    turtle.setposition(200,-230)
    turtle.write('.', font=style, align='center')
    
    stat=open("status.txt")
    status=stat.read()
    print("Welcome Back ADMIN")
    print()
    print("Server status=",status)
    print("\n"*2)
    print(''' Menu

             Server

             Update Data

             Member view

             Signout and quit

             ''')
    achoice()
