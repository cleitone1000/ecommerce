from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Username', [validators.Length(min=4, max=25)])
    username = StringField('User', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('Confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
