#Url_for
from flask import Flask, redirect, render_template, url_for,request
import os
from forms import LoginForm
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY']='EFOIKEJF9IEJFIE9JFIEJ'#Para formulario
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
    return render_template('plantilla.html')

elnombre=""

@app.route('/plantilla')
def plantilla():
    return render_template('plantilla2.html',nombre=elnombre)

@app.route('/form',methods=["GET","POST"])
def form():
    global elnombre
    form=SignupForm()
    if form.validate_on_submit():
         nombre=form.name.data
         apellidos=form.lastname.data
         contrasenia=form.password.data
         email=form.email.data
         elnombre=nombre
         print(nombre)
         return redirect(url_for("plantilla"))
    return render_template('form.html',form=form)

@app.route("/login",methods=['POST','GET'])
def route():
    form=LoginForm()
    if form.validate_on_submit():
         contrasenia=form.password.data
         email=form.email.data
         print("llegue")
         return redirect(url_for("plantilla"))
    return render_template('login.html',form=form)



if __name__=='__main__':
    os.environ['FLASK_ENV']="development"
    app.run(debug=True)

