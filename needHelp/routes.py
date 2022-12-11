from needHelp import app
from flask import render_template, redirect


@app.route('/')
@app.route('/home', methods=['POST'])
def home():
    return render_template('home.html')
