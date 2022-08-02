import csv
from scapy.all import *
from scapy.layers.inet import IP
from flask import get_template_attribute, render_template, Response, stream_with_context
import time
import multiprocessing as mp

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

    def analyze_pkt(pkt):
        print("listening traffic on 192.168.1.20")
        src_ip = pkt[IP].src
        ips = get_ips()
        found = False
        for ip in ips:
            if ip[0] == src_ip:
                for foundip in foundips:
                    if foundip[0] == src_ip:
                        found = True
                        break

                if found == False:
                    foundips.append(ip)
                    print("found ip: " + str(ip))
                found = False

    foundips = []
    def get_updates():
        time.sleep(1)
        print("updating 2")
        num = 1
        while True:
            print("updating time " + str(num))
            num = num + 1
            time.sleep(5)
            yield render_template("listen.html", IPS=foundips)
    def update_template():
        time.sleep(1)
        print("updating")
        return Response(stream_with_context(get_updates()))
    time.sleep(1)
    update_template()

    # p2 = mp.Process(target=update_template)
    # p2.start()
    # return Response(stream_with_context(get_updates))
    # sniff(filter="ip dst 192.168.1.20", prn=analyze_pkt)
