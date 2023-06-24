from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo: ', [validators.Length(min=4, max=50)])
    username = StringField('Usuário', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Nova Senha', [
        validators.DataRequired(),
        validators.EqualTo('[confirm](https://www.google.com/search?q=confirm)', message='As senhas não correspondem!')
    ])
    confirm = PasswordField('Repita a senha: ')
