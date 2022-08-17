from flask import Flask, render_template, Blueprint, request
from anti_virus import add_ip, get_ips
from scapy.all import *
from scapy.layers.inet import IP
from turbo_flask import Turbo
from app_forms import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
turbo = Turbo(app)
Bootstrap(app)
found_ips = []

@app.context_processor  
def inject_load():
    return {'IPS': found_ips}

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/listen", methods=['GET', 'POST'])
def listen():
    if request.method == 'POST':
        start_sniff()
    return render_template("listen.html")

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form)

@app.route('/signup')
def signup():
    return render_template('signup.html')

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

def start_sniff():
    print("listening traffic on 192.168.1.20")
    sniff(filter="ip dst 192.168.1.20", prn=analyze_pkt)