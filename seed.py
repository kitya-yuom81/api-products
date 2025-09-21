from app.db import SessionLocal, Base, engine
from app.models import Product


Base.metadata.create_all(bind=engine)


db = SessionLocal()
items = [
{"name": "Mouse", "price": 9.99, "in_stock": True, "category": "accessories"},
{"name": "Keyboard", "price": 19.99, "in_stock": True, "category": "accessories"},
{"name": "Laptop", "price": 599.0, "in_stock": False, "category": "computers"},
{"name": "Headphones", "price": 49.0, "in_stock": True, "category": "audio"},
]
for it in items:
    db.add(Product(**it))


db.commit()
db.close()
print("Seeded 4 products.")