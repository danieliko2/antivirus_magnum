from curses import def_prog_mode
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import socket
from scapy.all import *
from scapy.layers.inet import IP, UDP, Ether
import netifaces
from anti_virus import get_ips

# browser = webdriver.Firefox(executable_path="/home/john/Desktop/antivirus project/drivers/geckodriver")
# wait = WebDriverWait(browser, 3)
# visible = EC.visibility_of_element_located

# def testPage(page):
#     browser.get(page)
#     wait.until(visible((By.ID, "video-title")))
#     browser.find_element_by_id("video-title").click()
#     browser.minimize_window()
#     time.sleep(7)
#     browser.quit()

# def get_ips():
#     with open("data/data.csv", "r") as f:
#         csvRead = csv.reader(f)
#         rows = list(csvRead)
#         print(rows)

# get_ips()

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
