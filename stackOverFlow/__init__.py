from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET KEY'] = '04293911c5c5e7947afa3342ef59d6b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stack.db'
db = SQLAlchemy(app)
from stackOverFlow import routes