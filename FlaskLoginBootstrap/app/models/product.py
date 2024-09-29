from app import model_base_class
from app.core.sqlalchemy_base_model import SQLAlchemyBaseModel
from config import Config

class Product(model_base_class):
    if Config.DATABASE_TYPE == "sqlalchemy":
        __tablename__ = "product"

        id = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.Integer, primary_key=True)
        public_id = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.Integer, nullable=False)
        name = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.String(20), nullable=False, unique=True)
        price = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.Integer, nullable=False)

    elif Config.DATABASE_TYPE == "mongodb":
        collection_name = "products"

        def __init__(self, public_id=None, name=None, price=None):
            self.public_id = public_id
            self.name = name
            self.price = price

        def to_dict(self):
            d = {}

            if hasattr(self, "_id"):
                d["_id"] = self._id

            return {
                "public_id": self.public_id,
                "name": self.name,
                "price": self.price
            }
