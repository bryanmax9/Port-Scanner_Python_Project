# socket library allows us to stablish a connection over the internet
import socket
#intall it with command "pip3 install IPy" -> in my case "C:/Users/brill/AppData/Local/Microsoft/WindowsApps/python3.10.exe -m pip install IPy  "
from IPy import IP # we will use it in order for the user to put a domain name instead of using nslookup
import threading #for faster scanning port

thread_limit = 50  # Number of threads to use for port scanning
semaphore = threading.Semaphore(value=thread_limit)

def ip_scaner(target):
  converted_ip = check_ip(target)
  if not converted_ip:
    print(f"Skipping {target}...")
    return

  print(f"\n 🔎🔬scanning target: {converted_ip} \n")
  #scaning ports from 75 to 85
  for port in range(1, 1025):
    # Semaphore is used to limit the number of concurrent threads.
    # This ensures we don't overload the system with too many simultaneous scans.
    semaphore.acquire()

    # Creating a new thread to scan a specific port.
    # This allows multiple ports to be scanned concurrently (at the same time).
    t = threading.Thread(target=scan_port, args=(converted_ip, port))
    # Start the thread, making it begin its assigned task (in this case, scanning a port).
    t.start()


def check_ip(ip):

  try:
    # Stripping unnecessary parts of a potential URL to get the hostname
    if "http://" in ip or "https://" in ip:
      ip = ip.split("://")[1].split("/")[0]
          
    #Checking if it is an ip address
    IP(ip)
    return(ip)
  except ValueError:
    try:
      # Convert hostname to IP address
      return socket.gethostbyname(ip)
    except socket.gaierror:
      print(f"Failed to get IP address for {ip}. Is it a valid hostname?")
      return None

def get_port_description(port):
  port_descriptions = {
    20: 'FTP Data Transfer',
    21: 'FTP Command Control',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP Server',
    68: 'DHCP Client',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    123: 'NTP',
    137: 'NETBIOS Name Service',
    138: 'NETBIOS Datagram Service',
    139: 'NETBIOS Session Service',
    143: 'IMAP',
    161: 'SNMP',
    162: 'SNMPTRAP',
    443: 'HTTPS',
    445: 'Microsoft-DS',
    3389: 'RDP',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    27017: 'MongoDB'
  }
  return port_descriptions.get(port, 'Unknown Service')


def get_banner(s):
  #recieve data of the open port
  return s.recv(1024) 

def scan_port(ipaddress,port):
  try:


    #defining a socket descriptor
    sock = socket.socket()


    #some port may take long to connect to without timeout the acuracy will be high, the lower the timeout the smaller the accuracy
    # #this is to scan faster 
    sock.settimeout(0.5) #0.5 seconds
  
    #now we can try to connect to the target machine
    sock.connect((ipaddress, port))

    description = get_port_description(port)

    
    try:
      #Retrieve information of what softwarte is using
      banner = get_banner(sock)
      print(f"port {port} is open 🐧 using {banner} Software - {description}")
      
    except:
      print(f"port {port} is open 🐧 - {description}")


    
  except:
    #print(f"port {port} is closed 😥")
    pass
  finally:
    semaphore.release()



if __name__ == '__main__':
  #The pogram start here 🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜🦜
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
  ipaddress = input("💻Enter the Ip's address or domain name's of the target that you want to scan (split targets with ',' ): ")
  
  
  if ',' in ipaddress:
    #multiple targets
    for ip_add in ipaddress.split(','):
      ip_scaner(ip_add.strip(' '))
  
  else:
    #a single ip scanning
    ip_scaner(ipaddress)
 

  