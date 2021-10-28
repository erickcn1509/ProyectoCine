import sqlite3
from sqlite3 import Error
from flask import Flask



def comexion_sql():
    try:
        con = sqlite3.connect('cine.db')
        return con;
    except Error:
        print(Error) 
 

""" def comexion_sql():
    
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app """

def cerrar(con):
    con.close()

def insertar_usuario(nombre, apellido, sexo, identificacion, fecha_naci, celular, correo, password):
    try:
        con = comexion_sql()
        cursor = con.cursor()
        
        strsql = "INSERT INTO usuario (nombre, apellido, sexo, identificacion, fecha_naci, celular, correo, password) VALUES ('{}', '{}', '{}', '{}','{}', '{}', '{}', '{}')".format(nombre, apellido, sexo, identificacion, fecha_naci, celular, correo, password)

        cursor.execute(strsql)
        con.commit()
        con.cerrar()
    except:
        print("An error has occured")