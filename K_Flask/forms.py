from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    name=StringField('Nombre',validators=[DataRequired(),Length(max=25)])
    lastname=StringField('Apellidos',validators=[DataRequired(),Length(max=25)])
    password=PasswordField('Contraseña',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Contraseña',validators=[DataRequired()])
    submit = SubmitField('Enviar')