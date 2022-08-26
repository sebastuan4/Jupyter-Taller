from flask import Flask, redirect, render_template, url_for,request
import os
app = Flask(__name__)#Main, app.py

@app.route("/pagina")#Vistas
def pagina():
    return("Hola mundo")

@app.route("/")
def index():
   return render_template("login.html")

@app.route("/info")
def home():
    return render_template("index.html")

@app.route("/<int:numero>",)
def index_numero(numero):
    return(f"Hola bienvenidos a la pagina principal {numero}")

if __name__=='__main__':
    os.environ['FLASK_DEBUG']="development"
    app.run(debug=True)