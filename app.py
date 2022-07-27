from doctest import testmod
from flask import Flask
from flask import render_template, request, jsonify
from anti_virus import print_me, add_ip, listen_traffic, get_ips
from scapy.all import *


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/listen", methods=['GET', 'POST'])
def listen():
    if request.method == 'POST':
        listen_traffic()
    return render_template("listen.html")

@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.is_json:
        text = request.args.get('test_text')
        return jsonify({'ip':'100.10.10.1'})

    # if request.is_json and request.id == "getIP":
    #     ipA = request.args.get('ipAdr')
    #     riskN = request.args.get('')
    #     return jsonify({'ip':'100.10.10.1'})

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
    # return('test')

def printer(ip):
    print_me("me!#")


ip = "123"
# sniff(filter="src 2a10:8003:43a0:0:9ac8:d870:5d89:32c0", prn=printer(ip)) 