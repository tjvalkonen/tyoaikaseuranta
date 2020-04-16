from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class AccountForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    username = StringField("Username", [validators.Length(min=2)])
    password = PasswordField("Password", [validators.Length(min=2)])
    role = SelectField("Role", choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')])
 
    class Meta:
        csrf = False
