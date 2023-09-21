# socket library allows us to stablish a connection over the internet
import socket
#intall it with command "pip3 install IPy" -> in my case "C:/Users/brill/AppData/Local/Microsoft/WindowsApps/python3.10.exe -m pip install IPy  "
from IPy import IP






def scan_port(ipaddress,port):
  try:
    #defining a socket descriptor
    sock = socket.socket()


    #some port may take long to connect to without timeout the acuracy will be high, the lower the timeout the smaller the accuracy
    # #this is to scan faster 
    sock.settimeout(0.5) #0.5 seconds
  
    #now we can try to connect to the target machine
    sock.connect((ipaddress, port))
    print(f"port {port} is open 🐧")
  except:
    print(f"port {port} is closed 😥")




if __name__ == '__main__':
  #The pogram start her 🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜
  #if we want to scan the port of a website, then copyt the url and use this commands:
  # "nslookup https://www.google.com/"
  #
  # displays:
  # Server:  UnKnown
  # Address:  2600:6c50:7a3f:4825::1

  # Name:    https://www.google.com/.lan
  # Address:  192.168.1.1


  # copy "192.168.1.1" and use it in the program 👌😅👍

  #store ip of the machine or server that we are trying to scan 
  ipaddress = input("💻Enter the Ip address of the target that you want to scan: ")

  for port in range(75,85):
    scan_port(ipaddress,port)