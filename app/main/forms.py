from flask_wtf import Form
from wtforms.fields import StringField, SubmitField, TextField, BooleanField, PasswordField, TextAreaField
from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators, StringField
from wtforms.validators import DataRequired
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
