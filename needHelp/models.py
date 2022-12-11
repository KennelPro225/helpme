from needHelp import db
from datetime import datetime


class User(db.Model):
    id = db.Column('userId', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30),
                         unique=True, nullable=False)
    email = db.Column('userMail', db.String(),
                      unique=True, nullable=False)
    password = db.Column('password', db.String, nullable=False)
    occupation = db.Column('occupation', db.Integer, nullable=False)
    location = db.Column('location', db.Integer, nullable=False)
    date = db.Column('date', db.DateTime(default=datetime.utcnow()))
    post = db.relationship('Post', backref='user', lazy=True)


class Post(db.Model):
    id = db.Column('postId', db.Integer, primary_key=True)
    content = db.Column('postContent', db.String)
    title = db.Column('postTitle', db.String)
    author = db.Column('author', db.Integer, db.ForeignKey('user.id'))
    date = db.Column('date', db.DateTime(default=datetime.utcnow()))


class Interaction(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    author = db.Column('author', db.Integer)
    comment = db.Column('post', db.Integer, db.ForeignKey('comment.id'))


class Comment(db.Model):
    id = db.Column('commentId', db.Integer, primary_key=True)
    content = db.Column('commentContent', db.String)
    title = db.Column('commentTitle', db.String)
    author = db.Column('author', db.Integer, db.ForeignKey('user.id'))
    interaction = db.relationship('Interaction', backref='comment', lazy=True)
    date = db.Column('date', db.DateTime(default=datetime.utcnow()))
