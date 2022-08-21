from flask import Flask, render_template, Blueprint, request, redirect, url_for
from anti_virus import add_ip, get_ips
from scapy.all import *
from scapy.layers.inet import IP
from turbo_flask import Turbo
from app_forms import LoginForm, RegisterForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "appkeys88!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/john/Desktop/antivirus_project/database.db'

turbo = Turbo(app)
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

found_ips = []

@app.context_processor  
def inject_load():
    return {'IPS': found_ips}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home2():
    return render_template("home.html")

@app.route("/listen", methods=['GET', 'POST'])
@login_required
def listen():
    if request.method == 'POST':
        start_sniff()
    return render_template("listen.html")

@app.route("/config", methods=['GET', 'POST'])
@login_required
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
    return render_template("ip_list.html", IPS=ips)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for("home"))
        # return '<h1>' + form.username.data + " " + form.password.data + "</h1>"
        return '<h1> invalid username or password </h1>'
    print(current_user)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> new user has been created </h1>'
        # return '<h1>' + form.username.data + " " + form.password.data + "</h1>"

    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


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

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))