from flask import Flask
from flask import render_template, request, jsonify, get_template_attribute, Response, stream_with_context, render_template_string
from anti_virus import print_me, add_ip, listen_traffic, get_ips
from scapy.all import *
from testing import jinja2_render_test

## start with sudo flask run!

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/listen", methods=['GET', 'POST'])
def listen():
    if request.method == 'POST':
        listen_traffic()
    return render_template("listen.html", IPS=[]) # currently showing all ips

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

@app.route("/testing", methods=['GET', 'POST'])
def testing():
    if request.method == 'POST':
        # return(jinja2_render_test())
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
                yield render_template("testing.html", IPS=ips)
                num = num + 1
                time.sleep(2)

        return Response(stream_with_context(print_ip()))

    if request.method == 'GET':
        return render_template("testing.html")
    
@app.route("/abc")
def server_1():
    def generate_output():
        age = 0
        template = '<p>{{ name }} is {{ age }} seconds old.</p>'
        context = {'name': 'bob'}
        while True:
            context['age'] = age
            yield render_template_string(template, **context)
            time.sleep(5)
            age += 5

    return Response(stream_with_context(generate_output()))

ip = "123"
# sniff(filter="src 2a10:8003:43a0:0:9ac8:d870:5d89:32c0", prn=printer(ip)) 