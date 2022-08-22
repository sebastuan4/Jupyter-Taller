#Urls y parametros
from tkinter.tix import Tree
from flask import Flask, render_template, url_for
import os
app = Flask(__name__)
empleados=['Maria','Kimberly','Alan','Richard']

usuarios={'Maria':['Alejandra Vargas','mariale19','Femenino']
,'Kimberly':['Chacon Rokas','susu36','Femenino']
,'Alan':['Chacon Rokas','susu36','Femenino']
,'Richard':['Chacon Rokas','susu36','Femenino']}

@app.route('/')#Url nuevo
def index():
    return render_template('index.html',numero_empleados=empleados[0])
    

@app.route('/segundo')
def segundo():
    return "Esta es nuestra segunda pagina"

@app.route('/usuario/<int:index>')
def usuario(index):
    return str(empleados[index])

@app.route('/datos/<string:index>/<int:index2>')
def datos(index,index2):
    return str(usuarios[index][index2])

@app.route('/defecto/')
@app.route('/defecto/<string:index>')
def datosDefecto(index=0):
    return str(index)

if __name__=='__main__':
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)

