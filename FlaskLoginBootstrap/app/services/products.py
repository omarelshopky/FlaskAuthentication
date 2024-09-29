import uuid
from app.models.product import Product


class ProductService:
    def get_all(self):
        return Product.select_all()

    def create(self, name, price):
        product = Product(public_id=str(uuid.uuid4()), name=name, price=price)
        product.insert()

    def get_by_public_id(self, public_id):
        return Product.select({"public_id": public_id}, only_one=True)

    def update(self, product, name, price):
        product.name = name
        product.price = price

        product.update()

    def delete(self, product):
        product.delete()

