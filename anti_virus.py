import csv
from flask import Blueprint

anti_virus = Blueprint('anti_virus', __name__)

def add_ip(ipData):
    with open("data/data.csv", "a") as f:
        write = csv.writer(f)
        write.writerow(ipData)

def get_ips():
    with open("data/data.csv", "r") as f:
        csvRead = csv.reader(f)
        rows = list(csvRead)
        return rows


    # def analyze_pkt(pkt):
    #     print("listening traffic on 192.168.1.20")
    #     src_ip = pkt[IP].src
    #     ips = get_ips()
    #     found = False
    #     for ip in ips:
    #         if ip[0] == src_ip:
    #             for foundip in foundips:
    #                 if foundip[0] == src_ip:
    #                     found = True
    #                     break

    #             if found == False:
    #                 foundips.append(ip)
    #                 print("found ip: " + str(ip))
    #             found = False

    # def get_updates():
    #     time.sleep(1)
    #     print("updating 2")
    #     num = 1
    #     while True:
    #         print("updating time " + str(num))
    #         num = num + 1
    #         time.sleep(5)
    #         yield render_template("listen.html", IPS=foundips)

    # def update_template():
    #     while True:

    #         time.sleep(1)
    #         print("updating")
    #         return Response(stream_with_context(get_updates()))

    # time.sleep(1)
    # update_template()
