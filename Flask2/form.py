from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Email, Length


class registro(FlaskForm):
    name=StringField('Nombre',validators=[DataRequired(),Length(max=25)])
    lastname=StringField('Apellidos',validators=[DataRequired(),Length(max=55)])
    password=PasswordField('Contraseña',validators=[DataRequired(),Length(min=8)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Resgistrarse')
class login(FlaskForm):
    pass