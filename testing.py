import socket
from scapy.all import *
from scapy.layers.inet import IP
import netifaces
from anti_virus import get_ips
from flask import stream_with_context, Response, render_template
import time
# print(IFACES)

# hostname=socket.gethostname()
# IPAddr=socket.gethostbyname(hostname)
# print("Your Computer Name is:"+hostname)
# print("Your Computer IP Address is:"+IPAddr)
# print("Total Interfaces : {}".format(len(netifaces.interfaces())))
# print(socket.gethostbyname('github.com'))

# ips = get_ips()
# def listen_traffic(pkt):
#     src_ip = pkt[IP].src
#     for ip in ips:
#         if ip[0] == src_ip:
#             print("found ip: " + str(ip))
# sniff(filter="ip dst 192.168.1.20", prn=listen_traffic)

def jinja2_render_test():
    def print_ip():
        num = 1
        ips = ['new ip','second new ip']

        while True:
            print("testing rendering #" +str(num))
            # env = Environment(
            #     loader=FileSystemLoader('templates'),
            #     autoescape=select_autoescape(['html', 'xml'])
            # )
            # template = env.get_template('testing.html')

            ips.append(num)
            render_template("testing.html", IPS=ips)
            num = num + 1
            time.sleep(2)
            render_template("testing.html")

    return Response(stream_with_context(print_ip()))
    
