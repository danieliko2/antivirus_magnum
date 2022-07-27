import socket
from scapy.all import *
from scapy.layers.inet import IP
import netifaces
from anti_virus import get_ips


print(IFACES)

hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)
print("Total Interfaces : {}".format(len(netifaces.interfaces())))
print(socket.gethostbyname('github.com'))

ips = get_ips()
def listen_traffic(pkt):
    src_ip = pkt[IP].src
    for ip in ips:
        if ip[0] == src_ip:
            print("found ip: " + str(ip))
sniff(filter="ip dst 192.168.1.20", prn=listen_traffic)
