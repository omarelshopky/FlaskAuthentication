from flask_sqlalchemy import SQLAlchemy
from flask_injector import inject
import uuid
from app.models.product import Product


class ProductService:
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_all(self):
        return Product.query.all()

    def get_by_public_id(self, public_id):
        return Product.query.filter_by(public_id=public_id).first()

    def get_by_name(self, name):
        return Product.query.filter_by(name=name).first()

    def create(self, name, price):
        product = self.get_by_name(name)

        if product:
            return False

        product = Product(public_id=str(uuid.uuid4()), name=name, price=price)
        self.db.session.add(product)
        self.db.session.commit()

        return True

    def update(self, product, name, price):
        product.name = name
        product.price = price
        self.db.session.commit()

        return product

    def delete(self, product):
        self.db.session.delete(product)
        self.db.session.commit()

