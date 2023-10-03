print("Login")
print("^^^^^^")
a=open("D:\\COVID 19 project csc\\20.csv")
c=a.readlines()
d = {}
for i in range(0,len(c)):
    x=c[i]
    (key, val)= x.split(":")
    d[key]= val.rstrip("\n")
username=input("Username= ")

for j in d:
    if j==username:
        print("your passsword((for checking only)=",d[j])
        password=input("Password= ")
        if password==d[j]:
            print("Welcome Back",username)
            break
        else:
            print("Incorrect password")
            break
else:
    print("usernasme not found")
    

    
    
