from googlesearch import search
import socket
import bcolors

print("------------------------------------------------")
print("Code BY ::  NG")
print("------------------------------------------------")

url = input(bcolors.BLUE + "Enter URL which Subdomain we want to find by using GOOGLE dork Functionality ")

if(url.startswith("https://")):
  new_url = url.replace("https://", "*.")
else:
  new_url = url.replace("http://", "*.")

surl = new_url
surl= "site:" + new_url
host_ip = socket.gethostbyname(new_url)

try:
    from googlesearch import search
except ImportError:
    print("Not found")

limit = int(input(bcolors.HEADER +  "Please enter the limit how many SubDomain you want to fetch"))

portScanLowerLimit = int(input(bcolors.HEADER + "Please enter the starting value of port scan"))
portScanUpperLimit = int(input(bcolors.HEADER + "Please enter the end value of scan"))

for u in search(surl, tld="com", num=10, stop=limit, pause=2):
    if (u.startswith("https://")):
        u_sub_port = u.replace("https://", "")
    else:
        u_sub_port = u.replace("http://", "")
    for port in range(portScanLowerLimit,portScanUpperLimit):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = sock.connect_ex((host_ip, port))
        if connect == 0:
            print("Port {}:    is Open".format(port))
            print(bcolors.OKMSG + u_sub_port)
            sock.close()


