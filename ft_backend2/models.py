
from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime 


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

   
    products = db.relationship('Product', backref='user', lazy=True)



