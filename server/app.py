from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token, JWTManager
from flask_restful import Api, Resource, reqparse
from datetime import datetime 
import bcrypt
from flask_cors import CORS
from flask import send_from_directory


app = Flask(__name__)
# app.static_folder = "images"
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Threadup.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
api = Api(app)

from models import User, Product  # Import your User and Product models

# ...

# Define User Registration Resource
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
# Define User Login Resource
class UserLoginResource(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()

        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
            # Generate an access token using JWT
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401


api.add_resource(UserLoginResource, '/login')

# Define Product Resource
class ProductResource(Resource):
    def post(self):
        data = request.get_json()

        # Extract product data from 'data'
        product_name = data.get('product_name')
        product_image = data.get('product_image')
        user_id = data.get('user_id')
        size = data.get('size')
        category = data.get('category')
        price = data.get('price')

        # Create a new product in the database
        new_product = Product(
            product_name=product_name,
            product_image=product_image,
            user_id=user_id,
            size=size,
            category=category,
            price=price,
            in_stock=True,  # Set 'in_stock' to True for newly created products
            created_at=datetime.now(),  # Set the creation timestamp
            updated_at=datetime.now()  # Set the update timestamp
        )

        db.session.add(new_product)
        db.session.commit()

        return {'message': 'Product created successfully'}, 201

    def get(self):
        # Query the database to fetch all products
        products = Product.query.all()

        # Convert the list of products to a JSON response
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

# Define Product Deletion Resource
class ProductDeletionResource(Resource):
    def delete(self, product_id):
        # Fetch the product by ID
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404

        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted successfully'}, 204
api.add_resource(ProductDeletionResource, '/product/<int:product_id>')
# Define User Deletion Resource
class UserDeletionResource(Resource):
    def delete(self, user_id):
        # Fetch the user by ID
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}, 204

api.add_resource(UserDeletionResource, '/user/<int:user_id>')


@app.route('/get-image/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(debug=True)

