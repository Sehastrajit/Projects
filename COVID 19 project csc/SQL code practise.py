import sqlite3 as sqlite
import time
def retry():
    print()
    a=input("Continue? = ")
    if a == "y" or a =="Y":
        SQL()
    else:
        exit
def tableview(i):
        if len(i)==7:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|",i[3]," "*(8-len(str(i[3]))),"|",i[4]," "*(7-len(str(i[4]))),"|",i[5]," "*(7-len(str(i[5]))),"|",i[6]," "*(10-len(str(i[6]))),"|")
        elif len(i)==6:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|",i[3]," "*(8-len(str(i[3]))),"|",i[4]," "*(7-len(str(i[4]))),"|",i[5],"|")
        elif len(i)==5:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|",i[3]," "*(8-len(str(i[3]))),"|",i[4]," "*(7-len(str(i[4]))),"|")
        elif len(i)==4:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|",i[3]," "*(8-len(str(i[3]))),"|")
        elif len(i)==3:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|")
        elif len(i)==2:
            print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(8-len(str(i[1]))),"|")
        elif len(i)==1:
            print("|",i[0],"|")
        else:
            print("u r dumb")
def SQL():
    con = sqlite.connect('covid191.db')
    cur = con.cursor()
    print("SAMPLE CODE -> SELECT * FROM covid191 WHERE DEATH >1000;")
    print()
    query=input("Enter the SQL code=")
    a=cur.execute(query)
    z=cur.fetchone()
    z=cur.fetchone()
    z=cur.fetchone()
    d=int(z[3])
    print(d*3)
    print("_"*98,end="\n")
    global i
    L=["Country","INFECTED","DEATH","RECOVERY" , "Active" ,"Serious" ,"Tot. Tests "]
    c=len(z)
    L=L[0:c]
    tableview(L)
    print("_"*98,end="\n")
    for i in z:
        i=list(i)
        tableview(i)
    print("_"*98,end="\n")
    con.commit()
    con.close()
    print()
    retry()
SQL()
t=int(input("Type 0 to end view table"))
print()
time.sleep(t)
