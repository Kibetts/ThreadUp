from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_restful import Api, Resource, reqparse

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

        # Check if username or email already exists
        existing_user = User.query.filter((User.username == data['username']) | (User.email == data['email'])).first()
        if existing_user:
            return {'message': 'Username or email already exists'}, 400

        # Hash the password
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        # Create a new user
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hashed_password.decode('utf-8'),
            # Add other user attributes here
        )

        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


api.add_resource(UserRegistrationResource, '/register')
