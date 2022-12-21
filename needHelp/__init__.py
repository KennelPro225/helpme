from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd4f617ad7b2226da176f1c276cf87562435bcb259cf483512c5f2dedba34113d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///needhelp.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from needHelp import routes
