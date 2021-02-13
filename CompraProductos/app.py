from flask import Flask
import mysql.connector
app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='productos')
cursor = cnx.cursor()

@app.route('/')
def hello_world():
    cant1 = 10
    cant2 = 20
    mydict = {}
    query = (""" select * from producto 
                 where precio between %s and %s; """)
    cursor.execute(query, (cant1, cant2))
    for (ID, NOM, PRE, STK) in cursor:
        mydict[str(ID)] = {"nombre": NOM, "precio": PRE, "stock": STK}
        print("{}, {}, {}, {}".format(
            ID, NOM, PRE, STK))
    return mydict

if __name__ == '__main__':
    app.run()