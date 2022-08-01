#Sirve para crear aplicaciones de arquitectura MVC Modules Views Controler
#Modelo--Datos, base de datos-capa de datos
#Vista--Interfaz de usuario-capa de gui
#Controlador--Gestiona las dos partes-capa de negocio
#set-executionpolicy remotesignes
#pip install virtualenv
#pip install flask
#env/Scrips/Activate
#static-css
#templates
from tkinter.tix import Tree
from flask import Flask, render_template, url_for
import os
app = Flask(__name__)
empleados=['Maria','Kimberly']
@app.route('/')#Vista
def index():
    return render_template('index.html',numero_empleados=empleados[1])

if __name__=='__main__':
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)