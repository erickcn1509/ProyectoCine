from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def funcion():
    return render_template('registro.html')