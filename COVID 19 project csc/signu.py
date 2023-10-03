d={}
def signup():
    print("signup")
    print("^^^")
    global newpass,repass,newuser
    newuser=input("Username=")
    newpass=input("Choose Password=")
    repass=input("Reenter Password=")

signup()
if newpass==repass:
    d[newuser]=newpass
    print("account suceefully created")
    login()
else:
    signup()
