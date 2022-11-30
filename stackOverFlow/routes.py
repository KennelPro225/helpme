from stackOverFlow import app
# from stackOverFlow.models import Users
from flask import render_template, redirect


@app.route('/')
@app.route('/home', methods=['POST'])
def home():
    return render_template('home.html')
