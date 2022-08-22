from flask import Flask, redirect, render_template, url_for,request
import os
from form import registro
app = Flask(__name__)
app.config['SECRET_KEY']="FIEJFIEJFOWIFJWOF"
@app.route("/") 
def index():
    return("Hola mundo")

@app.route("/ruta2") 
def ruta2():
    return("8000")

@app.route("/registro",methods=['POST','GET']) 
def parametro():
    form = registro()
    if form.validate_on_submit():
        name=form.name.data
        lastname=form.lastname.data
        password=form.password.data
        email=form.email.data
        print(name)
        return("registrado")
    return render_template("login.html",form=form)

@app.route("/login") 
def login():
    return render_template("login.html")

if __name__ == "__main__":
    os.environ["FLASK_ENV"]="development"
    app.run(debug=True)
