
from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime 


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

   
    products = db.relationship('Product', backref='user', lazy=True)


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    size = db.Column(db.String(50))
    category = db.Column(db.String(255))
    price = db.Column(db.Float)
    in_stock = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

