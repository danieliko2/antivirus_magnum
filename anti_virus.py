import csv
from scapy.all import *
from scapy.layers.inet import IP

foundips=[]

def print_me(me):
    print(me)

print("")

def add_ip(ipData):
    with open("data/data.csv", "a") as f:
        write = csv.writer(f)
        write.writerow(ipData)

def get_ips():
    with open("data/data.csv", "r") as f:
        csvRead = csv.reader(f)
        rows = list(csvRead)
        return rows

def listen_traffic():
    ips = get_ips()
    print("listening traffic on 192.168.1.20")
    def analyze_pkt(pkt):
        src_ip = pkt[IP].src
        for ip in ips:
            if ip[0] == src_ip:
                print("found ip: " + str(ip))
                foundips.append(ip)

    sniff(filter="ip dst 192.168.1.20", prn=analyze_pkt)
    