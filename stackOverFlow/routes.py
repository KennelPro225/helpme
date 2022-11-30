from stackOverFlow import app, db
from stackOverFlow.models import Users
from flask import render_template, redirect


@app.route('/')
@app.route('/home', methods=['POST'])
def home():
    try:
        user = Users('Kennel', 12)
        dbResponse = db.users.insert_one(user)
    except Exception as exception:
        print(exception)
    return render_template('home.html')
