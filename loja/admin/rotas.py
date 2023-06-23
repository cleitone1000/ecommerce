from flask import render_template, session, request, url_for, flash

from loja import app, db, bcrypt

from .formulario import RegistrationForm

import os








@app.route('/')

def home():
    return "Hello World!"


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Obrigado por registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='Pagina de registros')
