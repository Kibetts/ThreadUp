from app import app, db, Product
from models import Product

products_data = [
    {
        "product_name": "Rugged trousers",
        "product_image": "images/tamara-bellis-zDyJOj8ZXG0-unsplash.jpg",
        "user_id": 1,  # Replace with the actual user ID
        "size": "Medium",
        "category": "Clothing",
        "price": 49.99,
        "in_stock": True,
        # Add other product attributes
    },
    {
        "product_name": "Sneakers",
        "product_image": "images/kris-gerhard-0BKZfcamvGg-unsplash.jpg",
        "user_id": 2,  # Replace with the actual user ID
        "size": "Large",
        "category": "Clothing",
        "price": 50.99,
        "in_stock": True,
        # Add other product attributes
    },
        {
        "product_name": "Vans",
        "product_image": "images/paul-gaudriault-a-QH9MAAVNI-unsplash.jpg",
        "user_id": 3,  # Replace with the actual user ID
        "size": "XXL",
        "category": "Shoes",
        "price": 100.99,
        "in_stock": True,
        # Add other product attributes
    },
      {
        "product_name": "Skechers",
        "product_image":"images/the-dk-photography-APKtyf7MDR4-unsplash.jpg",
        "user_id": 4,  # Replace with the actual user ID
        "size": "XXL",
        "category": "Shoes",
        "price": 1000.99,
        "in_stock": True,
        # Add other product attributes
    },
]
def seed_products():
    with app.app_context():  # Create an application context
        for data in products_data:
            product = Product(**data)
            db.session.add(product)
        db.session.commit()  # Commit all changes after adding products

if __name__ == "__main__":
    seed_products()
