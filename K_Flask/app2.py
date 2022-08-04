#Url_for
from tkinter.tix import Tree
from flask import Flask, render_template, url_for
import os
app = Flask(__name__)
empleados=['Maria','Kimberly','Alan','Richard']

usuarios={'Maria':['Alejandra Vargas','mariale19','Femenino']
,'Kimberly':['Chacon Rokas','susu36','Femenino']
,'Alan':['Chacon Rokas','susu36','Femenino']
,'Richard':['Chacon Rokas','susu36','Femenino']}

@app.route('/<int:numero>')
def index(numero):
    return render_template('index2.html',numero_empleados=empleados[numero])
@app.route('/linkqueado')
def link():
    return render_template('index2.html',numero_empleados=empleados[0])



if __name__=='__main__':
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)

