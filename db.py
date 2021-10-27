import sqlite3
from sqlite3 import Error

def comexion_sql():
    try:
        con = sqlite3.connect('cine.db')
        return con;
    except Error:
        print(Error) 

def cerrar(con):
    con.close()