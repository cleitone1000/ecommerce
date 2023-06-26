from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


#create the extension
db = SQLAlchemy()
#create de app
app = Flask(__name__)
#configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
app.config['SECRET_KEY'] = 'password'
#initialize the app with the extension
db.init_app(app)
bcrypt = Bcrypt(app)

from loja.admin import rotas
