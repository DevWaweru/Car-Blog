import os, jwt
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int)

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(48), unique = True, index=True)
    email = db.Column(db.String(48),unique=True, index = True)
    hash_pass = db.Column(db.String(255)) 

class Blog(db.Model):
    __tablename__='blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    blog_content = db.Column(db.String())
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    blog_picture = db.Column(db.String())
    
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    photo = db.relationship('Photo', backref='blog',lazy='dynamic')

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    comment_content = db.Column(db.String())
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

class Email(db.Model):
    __tablename__='emails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email_data = db.Column(db.String(255))

class Photo(db.Model):
    __tablename__='photos'
    id = db.Column(db.Integer,primary_key=True)
    photo_data = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))