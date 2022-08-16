from flask import Flask
from flask import render_template, request, jsonify, get_template_attribute, Response, stream_with_context, render_template_string
from anti_virus import add_ip, get_ips
from scapy.all import *
from scapy.layers.inet import IP
from testing import jinja2_render_test
from turbo_flask import Turbo
import threading

## start with sudo flask run!

app = Flask(__name__)
turbo = Turbo(app)

found_ips = []

@app.context_processor  
def inject_load():
    return {'IPS': found_ips}

# @app.before_first_request
# def before_first_request():
    # threading.Thread(target=start_sniff).start()


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/listen", methods=['GET', 'POST'])
def listen():
    if request.method == 'POST':
        start_sniff()
    return render_template("listen.html") # currently showing all ipsm

@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        ipA = request.form['ipAdr']
        riskN = request.form['riskN']
        comments = request.form['comments']
        ipData = [ipA, riskN, comments]
        add_ip(ipData)
        print("ip added: " + str(ipA))

    return render_template("config.html")

@app.route("/list_ips")
def list_ips():
    ips = get_ips()
    print(ips)
    return (str(ips))

def analyze_pkt(pkt):
    src_ip = pkt[IP].src
    ips = get_ips()
    found = False
    for ip in ips:
        if ip[0] == src_ip:
            for foundip in found_ips:
                if foundip[0] == src_ip:
                    found = True
                    break

            if found == False:
                found_ips.append(ip)
                print("found ip: " + str(ip))
                turbo.push(turbo.replace(render_template('foundips.html'), 'found_ips'))
            found = False
    # time.sleep(3)
    # with app.app_context():
    #     turbo.push(turbo.replace(render_template('foundips.html'), 'found_ips'))
    # print(found_ips)

def start_sniff():
    print("listening traffic on 192.168.1.20")
    sniff(filter="ip dst 192.168.1.20", prn=analyze_pkt)