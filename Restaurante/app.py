from random import random
from flask import request, render_template
import requests

from flask import Flask

app = Flask(__name__)
DAT = {}


def setdatos(d):
    DAT.update(d)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_datos')
def get_datos():
    return DAT


@app.route('/sendDatos', methods=['POST'])
def sendDatos():
    if request.method == 'POST':
        id_usr = request.form['id_usr']
        url = "http://localhost:8081"
        dat = {'id_usr': id_usr}
        setdatos(dat)
        r = requests.get(url=url, params=dat)

        return r.json()
    return "no Entro aca"
