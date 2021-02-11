from flask import request, render_template
import requests
import urllib.request
import os

from flask import Flask

app = Flask(__name__)
DAT = {'id_usr': 10, "raza": "boxer"}


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_datos')
def get_datos():
    return DAT


@app.route('/guardarimagen', methods=['POST'])
def guardar_imagen():
    url = request.json['url']
    # url = "https://images.dog.ceo/breeds/labrador/n02099712_3776.jpg"
    urllib.request.urlretrieve(url, "static/img/perro.jpg")
    return {'path': os.path.abspath("static/img/perro.jpg")}


@app.route('/sendDatos', methods=['POST'])
def sendDatos():
    if request.method == 'POST':
        id_usr = request.form['id_usr']
        raza = request.form['raza']
        dat = {'id_usr': id_usr, "raza": raza}
        DAT.update(dat)
        url = "http://localhost:8081"
        r = requests.get(url=url, params=dat)
        r = r.json()
        return render_template("index.html", datos=r)
    return "no Entro aca"
