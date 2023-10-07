from app import app, db, Product
from models import Product

products_data = [
    {
        "product_name": "Rugged trousers",
        "product_image": "https://images.unsplash.com/photo-1520517238863-2a437c6b1b08?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzl8fGplYW5zfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 1,  
        "size": "Medium",
        "category": "Clothing",
        "price": 49.99,
        "in_stock": True,
    },
    {
        "product_name": "Sneakers",
        "product_image": "https://images.unsplash.com/photo-1549298916-f52d724204b4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8c25lYWtlcnN8ZW58MHwwfDB8fHww&auto=format&fit=crop&w=500&q=60",
        "user_id": 2, 
        "size": "Large",
        "category": "Clothing",
        "price": 50.99,
        "in_stock": True,
    },
        {
        "product_name": "Vans",
        "product_image": "https://images.unsplash.com/photo-1512990414788-d97cb4a25db3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8dmFuc3xlbnwwfDB8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 3,  
        "size": "XXL",
        "category": "Shoes",
        "price": 100.99,
        "in_stock": True,
    },
        {
        "product_name": "Rugged trousers", 
        "product_image": "https://images.unsplash.com/photo-1582552938357-32b906df40cb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGplYW5zfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 4,
        "category": "Clothing",
        "size": "Medium", 
        "price": 49.99,
        "in_stock": True
        
        
    },
    {
        "product_name": "Blue jeans",
        "product_image": "https://plus.unsplash.com/premium_photo-1674828601362-afb73c907ebe?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8ZGVuaW18ZW58MHwxfDB8fHww&auto=format&fit=crop&w=500&q=60", 
        "user_id": 5,
        "category": "Clothing",
        "size": "32x30",
        "price": 59.50,
        "in_stock": True
    },
    {
        "product_name": "Yoga leggings",
        "product_image": "https://images.unsplash.com/photo-1534366352488-8b7b5f205086?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fHlvZ2ElMjBwYW50c3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 6,
        "category": "Clothing",
        "size": "Small",
        "price": 29.99,
        "in_stock": True
    },
    {
        "product_name": "Black t-shirt",
        "product_image": "https://images.unsplash.com/photo-1618354691551-44de113f0164?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fGJsYWNrJTIwdCUyMHNoaXJ0fGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 7,
        "category": "Clothing",
        "size": "Large",
        "price": 9.99,
        "in_stock": True
    },
    {
        "product_name": "Polka dot dress",
        "product_image": "https://images.unsplash.com/photo-1646277379248-bdbf06f4ed18?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cG9sa2ElMjBkb3QlMjBkcmVzc3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 8,
        "category": "Clothing",
        "size": "Medium",
        "price": 49.95,
        "in_stock": True
    },
    {
        "product_name": "Pink blouse",
        "product_image": "https://images.unsplash.com/photo-1591382010022-bb9dc3d368ce?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGJsb3VzZXxlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 9,
        "category": "Clothing",
        "size": "Small",
        "price": 24.50,
        "in_stock": True
    },
    {
        "product_name": "Nike running shoes",
        "product_image": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bmlrZSUyMHNob2VzfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 10,
        "category": "Shoes",
        "size": "10",
        "price": 89.99, 
        "in_stock": True
    },
    {
        "product_name": "Black heels",
        "product_image": "https://images.unsplash.com/photo-1596702876489-9d11e5806161?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8YmxhY2slMjBoZWVsc3xlbnwwfDF8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "user_id": 11,
        "category": "Shoes",
        "size": "7",
        "price": 69.00,
        "in_stock": True
    },
    {
        "product_name": "Leather oxfords",
        "product_image": "https://images.unsplash.com/photo-1605812860427-4024433a70fd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8TGVhdGhlciUyMG94Zm9yZHN8ZW58MHwxfDB8fHww&auto=format&fit=crop&w=500&q=60",
        "user_id": 12,
        "category": "Shoes",
        "size": "10.5",
        "price": 149.99,
        "in_stock": True
    }
    
]

def seed_products():
    with app.app_context():
        for data in products_data:
            product = Product(**data)
            db.session.add(product)
        db.session.commit()  
if __name__ == "__main__":
    seed_products()
