from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_restful import Api, Resource, reqparse
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