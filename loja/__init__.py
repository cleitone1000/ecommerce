from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from loja.admin import rotas


#create de app
app = Flask(__name__)
#configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhaloja.db'
#create the extension
db = SQLAlchemy()
app.config['SECRET_KEY'] = 'password'
#initialize the app with the extension
db.init_app(app)
bcrypt = Bcrypt(app)


