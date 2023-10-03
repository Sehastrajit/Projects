import time
def statuscheck():
    stat=open("status.txt")
    status=stat.read()
    if status=="Activate" or status=="activate":
        return
    elif status=="Deactivate" or status=="deactivate":
        print("               Oops")
        print("               The servers are down")
        print()
        print("                      visit again later")
        time.sleep(3)
        exit()
    else:
        print("Oops...")
        print("Something went wrong")
        time.sleep(2)
        exit()


