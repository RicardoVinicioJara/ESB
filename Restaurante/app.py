from random import random
from flask import request, render_template
import requests

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/sendDatos', methods=['POST'])
def sendDatos():
    if request.method == 'POST':
        id_usr = request.form['id_usr']
        URL = "http://localhost:8081"
        PARAMS = {'id_usr': id_usr}
        r = requests.get(url=URL, params=PARAMS)
        return r.json()
    return "no Entro aca"


if __name__ == '__main__':
    app.run(port=5050)
