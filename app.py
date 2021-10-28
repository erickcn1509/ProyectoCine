from flask import Flask, render_template,request, redirect, jsonify, send_file, session
import db, io, werkzeug.security as ws
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cine.db'

mysql = MySQL(app)

@app.route('/')
def funcion():
    return render_template('index.html')

@app.route('/confiteria.html')
def funcion2():
    return render_template('confiteria.html')

@app.route('/cartelera.html')
def funcion3():
    return render_template('cartelera.html')

@app.route('/registro.html', methods=['GET', 'POST'])
def funcion4():
    if request.method == 'POST':
        details = request.form
        nombre = details['nombre']
        apellido = details['apellido']
        sexo = details['sexo']
        identificacion = details['identificacion']
        fecha_naci = details['fecha_naci']
        celular = details['celular']
        correo = details['correo']
        password = details['password']
        cur = db.comexion_sql()
        cursor = cur.cursor()
        cursor.execute("INSERT INTO usuario (nombre, apellido, sexo, identificacion, fecha_naci, celular, correo, password) VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(nombre, apellido, sexo, identificacion, fecha_naci, celular, correo, password))
        cur.commit()
        cur.close()
        return 'succes'
    return render_template('registro.html')

@app.route('/index.html')
def funcion5():
    return render_template('index.html')

@app.route('/ingresar.html', methods=['GET', 'POST'])
def funcion6(): 
    data = []
    if request.method == 'GET':
        cur = db.comexion_sql()
        cursor = cur.cursor()
        getData = cursor.execute("SELECT correo, password FROM usuario")
        data = getData.fetchall()
        
        print (data)
        cur.commit()
        cur.close()
    else:
        details2 = request.form
        correo_login = details2['correo_login']
        password_login = details2['password_login']
        for i in data:
            if i[0] == correo_login and i[1] == password_login:
                return 'sesión iniciada'
            else:
                return render_template('index.html')
        
    return render_template('ingresar.html')



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


