from needHelp import db
from datetime import datetime


class User(db.Model):
    id = db.Column('userId', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30),
                         unique=True, nullable=False)
    email = db.Column('userMail', db.String(),
                      unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)
    photoprofile = db.Column(
        'profilepicture', db.String, default='default.png')
    occupation = db.Column('occupation', db.Integer)
    location = db.Column('location', db.Integer)
    date = db.Column('date', db.DateTime, default=datetime.utcnow())


class Post(db.Model):
    id = db.Column('postId', db.Integer, primary_key=True)
    content = db.Column('postContent', db.String)
    title = db.Column('postTitle', db.String)
    image = db.Column('imagePost', db.String)
    author = db.Column('author', db.Integer)
    date = db.Column(db.DateTime, nullable=False,
                     default=datetime.utcnow)


class Comment(db.Model):
    id = db.Column('commentId', db.Integer, primary_key=True)
    content = db.Column('commentContent', db.String)
    title = db.Column('commentTitle', db.String)
    author = db.Column('author', db.Integer)
    post = db.Column('post', db.Integer)
    date = db.Column(db.DateTime, nullable=False,
                     default=datetime.utcnow)


class Interaction(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    author = db.Column('author', db.Integer)
    comment = db.Column('post', db.Integer)
    rate = db.Column('rate', db.Boolean)
