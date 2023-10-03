a=open("D:\\COVID 19 project csc\\202.txt")
c=a.readlines()
import time
d = {}
for i in range(0,len(c)):
    x=c[i]
    (key, val)= x.split(":")
    d[key]= val.rstrip("\n")
def login():
    print("Login")
    print("^^^^^^")
    a=open("D:\\COVID 19 project csc\\20.csv")
    c=a.readlines()
    username=input("Username= ")
    for j in d:
        if j==username:
            print("your passsword((for checking only)=",d[j])
            password=input("Password= ")
            if password==d[j]:
                print("Welcome Back",username)
                time.sleep(5)
                break
            else:
                print("Incorrect password")
                break
    else:
        print("usernasme not found")
        login()
def signup():
    def signupdetails():
        print("signup")
        print("^^^^^^^")
        global newpass,repass,newuser
        newuser=input("Username=")
        newpass=input("Choose Password=")
        repass=input("Re-enter Password=")
    signupdetails()
    if newpass==repass:
        d[newuser]=newpass
        print("account suceefully created")
        login()
    else:
        signup()
def startup():
    ask=input("Login/Signup/Exit=")
    if ask=="Login" or ask=="login":
        login()
    elif ask=="Signup" or ask=="signup":
        signup()
    elif ask=='Exit'or'exit':
        exit()
    else:
        print("wrong input")
        startup()
startup()
