#importing module
import socket
from datetime import datetime



#ADDING BANNER
def banner():
    print("*" * 50)
    print("scanning target: "+target)
    print("time startted: "+str(datetime.now()))
    print("*" * 50) 





#taking input from user

ip= input("Enter the Ip address: ")

#translate hostname to ipv4
target= socket.gethostbyname(ip) 
print("1.all port scan, \n2.manual port scan")
inp= int(input("please enter 1/2: "))
if inp == 1:
    banner()
        
    for p in range(20,100):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result= s.connect_ex((target,p))
        if result == 0:
            print(f"port {p} is open")
        s.close()

        
elif inp == 2:
    
    port=int(input("enter port number: "))
    banner()
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result= s.connect_ex((target,port))
    if result == 0:
        print(f"port {port} is open")
    s.close()

 
    













