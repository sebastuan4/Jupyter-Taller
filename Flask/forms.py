from importlib.metadata import requires
from mailbox import NoSuchMailboxError
from flask import Flask, redirect, render_template, url_for,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, Length
class registro(FlaskForm):
    nombre=StringField("Nombre",validators=[DataRequired,Length(min=2,max=25)])
    apellidos=StringField("Apellidos",validators=[DataRequired,Length(min=5,max=30)])
    email=StringField("Email",validators=[DataRequired,Email])
    contrasenia=PasswordField("Constraseña",validators=[DataRequired,Length(min=8,max=50)])
    enviar=SubmitField("Enviar Formulario")
class login():
    pass
class contacto():
    pass
