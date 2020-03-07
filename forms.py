from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    code = StringField('Matrícula', 
            validators=[DataRequired(), Length(min=7, max=7)])
    fname = StringField('Nome', 
            validators=[DataRequired(), Length(min=2, max=50)])
    lname = StringField('Sobrenome', 
            validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    cpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Salvar')

class LoginForm(FlaskForm):
    code = StringField('code', 
           validators=[DataRequired(), Length(min=7, max=7)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')