from flask_login import UserMixin
from app import model_base_class
from app.core.sqlalchemy_base_model import SQLAlchemyBaseModel
from config import Config

class User(model_base_class, UserMixin):
    if Config.DATABASE_TYPE == "sqlalchemy":
        __tablename__ = "user"

        id = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.Integer, primary_key=True)
        public_id = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.Integer, nullable=False)
        name = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.String(40), nullable=False)
        username = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.String(20), nullable=False, unique=True)
        password = SQLAlchemyBaseModel.db.Column(SQLAlchemyBaseModel.db.String(128), nullable=False)

    elif Config.DATABASE_TYPE == "mongodb":
        collection_name = "users"

        def __init__(self, public_id=None, name=None, username=None, password=None):
            self.public_id = public_id
            self.name = name
            self.username = username
            self.password = password

        def to_dict(self):
            d = {}

            if hasattr(self, "_id"):
                d["_id"] = self._id

            return {
                "public_id": self.public_id,
                "name": self.name,
                "username": self.username,
                "password": self.password
            }

        def get_id(self):
            return str(self._id)