from flask import Flask, render_template,jsonify, redirect
import db

app = Flask(__name__)

@app.route('/')
def funcion():
    return render_template('index.html')

@app.route('/confiteria.html')
def funcion2():
    return render_template('confiteria.html')

@app.route('/cartelera.html')
def funcion3():
    return render_template('cartelera.html')

@app.route('/registro.html')
def funcion4():
    return render_template('registro.html')

@app.route('/index.html')
def funcion5():
    return render_template('index.html')

@app.route('/<string:tabla>')
def index(tabla):
    
    datos = consulta_tabla(tabla)

    return jsonify(datos)

def consulta_tabla(tabla):
    con = db.comexion_sql()

    strsql = "select * from " + tabla
   
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    datos = cursorObj.fetchall()

    con.close()
    return datos