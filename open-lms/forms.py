# This is manually created could be inside the main Python file, but it is better to split these things up.

from flask_wtf import FlaskForm
from wtforms import StringField # Deze is geinstalleerd met de `python3 -m pip install flask-wtf`.
from wtforms import PasswordField # Dis is voor een passwoord.
from wtforms import SubmitField
from wtforms import BooleanField # Is a or False
from wtforms.validators import DataRequired # Deze informatie is voor data validatie, dit is een verplicht veld.
from wtforms.validators import Length
from wtforms.validators import Email # Voor deze importeer deze: `python3 -m pip install email_validator`
from wtforms.validators import EqualTo


# We will create Classes that will be converted into 

class RegistrationForm(FlaskForm): # The name `RegistrationForm, you can choose yourself, but this will be inherit from `FlaskForm` that has be imported above from `flask_wtf`.
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)]) # The `Username`, will be used as the label-field in the HTML.
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up!')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In!')

# We need a CSR-request. You have to do this in the FLASK_APP-file.


