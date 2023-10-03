def allstat():   
    import sqlite3 as sqlite
    import time
    import turtle

    con = sqlite.connect('covid19.db')
    cur = con.cursor()              

    global z,a
    con = sqlite.connect('covid191.db')
    cur = con.cursor()
    query="SELECT * FROM covid191"
    L=["Country","INFECTED","DEATH","RECOVERY" , "Active" ,"Serious" ,"Tot.Test "]
    print("_"*93,end="\n")
    print("|",L[0]," "*(22-len(str(L[0]))),"|",L[1]," "*(7-len(str(L[1]))),"|",L[2]," "*(6-len(str(L[2]))),"|",L[3]," "*(7-len(str(L[3]))),"|",L[4]," "*(7-len(str(L[4]))),"|",L[5]," "*(6-len(str(L[5]))),"|",L[6]," "*(9-len(str(L[6]))),"|")
    print("_"*93,end="\n")
    a=cur.execute(query)
    z=cur.fetchall()
    for i in z:
        i=list(i)
        print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(7-len(str(i[1]))),"|",i[2]," "*(6-len(str(i[2]))),"|",i[3]," "*(7-len(str(i[3]))),"|",i[4]," "*(7-len(str(i[4]))),"|",i[5]," "*(6-len(str(i[5]))),"|",i[6]," "*(9-len(str(i[6]))),"|")
        print("_"*93,end="\n")

    print()
    '''import graph'''
    t=int(input("Type 0 to end view table"))
    turtle.clear()

    time.sleep(t)
    con.commit()
    con.close()



