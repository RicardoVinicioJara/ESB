from flask import request, render_template
import requests
import urllib.request
import os

from flask import Flask

app = Flask(__name__)
DAT = {'tipo': 2, 'id_usr': 5, "raza": "boxer"}


# DAT = {}


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/error')
def error():
    return {"error": "error"}


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
        dat = {'tipo': 1, 'id_usr': id_usr, "raza": raza}
        DAT.update(dat)
        url = "http://localhost:8081"
        r = requests.get(url=url, params=dat)

        js = r.json()
        print(js)
        if js['estado']:
            return render_template("index.html", datos=js)
    return render_template("error.html")


@app.route('/getProductos', methods=['POST'])
def getProductos():
    if request.method == 'POST':
        cant1 = request.form['cant1']
        cant2 = request.form['cant2']
        stock = request.form['stock']
        dat = {'tipo': 2, 'cant1': cant1, "cant2": cant2, "stock": stock}
        DAT.update(dat)
        url = "http://localhost:8081"
        r = requests.get(url=url)
        js = r.json()
        lista = []
        list_id = list(js.keys())
        for i in list_id:
            lista.append([js[str(i)]['id'], js[str(i)]['nombre'], js[str(i)]['precio'], js[str(i)]['stock']])
        print(js)
        print(lista)
        return render_template("index.html", lista=lista)
