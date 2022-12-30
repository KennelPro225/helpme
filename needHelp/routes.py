from flask import render_template, redirect, request, flash, url_for
from needHelp import app, bcrypt, db
from needHelp.models import User
import requests
import json


def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


@app.route('/')
@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/signup', methods=['POST', 'GET'])
def SignUp():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['mail']
            if request.form['cpassword'] == request.form['password']:
                password = bcrypt.generate_password_hash(
                    request.form['password']).decode('utf-8')
                sign = User(username=username, email=email,
                            password=password, location=get_ip())
                db.session.add(sign)
                db.session.commit()
        except TypeError as err:
            print(err)
    return render_template('signup.html')


@app.route('/signin')
def SignIn():
    return render_template('login.html')


@app.route('/check', methods=['POST'])
def check():
    username = request.form['username']
    existing_user = User.query.filter_by(username=username).all()
    ex = []

    for i in existing_user:
        ex.append({'name': i.username,
                  'email': i.email})
    if len(ex) > 0:
        return json.dumps(ex)
    else:
        return False


@app.route('/profile')
def Share():
    return render_template('profile.html', back='Background.jpeg')
