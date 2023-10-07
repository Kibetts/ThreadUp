from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, JWTManager
from flask_restful import Api, Resource, reqparse
from datetime import datetime 
import bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Threadup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

from models import User, Product 

class UserRegistrationResource(Resource):
    def post(self):
        data = request.get_json()

        existing_user = User.query.filter((User.username == data['username']) | (User.email == data['email'])).first()
        if existing_user:
            return {'message': 'Username or email already exists'}, 400

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hashed_password.decode('utf-8'),
        )

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


api.add_resource(UserRegistrationResource, '/register')

class UserLoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
            
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401


api.add_resource(UserLoginResource, '/login')

class ProductResource(Resource):
    def post(self):
        data = request.get_json()

        product_name = data.get('product_name')
        product_image = data.get('product_image')
        user_id = data.get('user_id')
        size = data.get('size')
        category = data.get('category')
        price = data.get('price')

        new_product = Product(
            product_name=product_name,
            product_image=product_image,
            user_id=user_id,
            size=size,
            category=category,
            price=price,
            in_stock=True,  
            created_at=datetime.now(), 
            updated_at=datetime.now()  
        )

        db.session.add(new_product)
        db.session.commit()

        return {'message': 'Product created successfully'}, 201
    
    def get(self):
        products = Product.query.all()

        product_list = []
        for product in products:
            product_data = {
                'product_id': product.product_id,
                'product_name': product.product_name,
                'product_image': product.product_image,
                'user_id': product.user_id,
                'size': product.size,
                'category': product.category,
                'price': product.price,
                'in_stock': product.in_stock,
                'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S') if product.created_at else None,
                'updated_at': product.updated_at.strftime('%Y-%m-%d %H:%M:%S') if product.updated_at else None
            }
            product_list.append(product_data)

        return {'products': product_list}


api.add_resource(ProductResource, '/product')

class ProductDeletionResource(Resource):
    def delete(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404

        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted successfully'}, 204
api.add_resource(ProductDeletionResource, '/product/<int:product_id>')