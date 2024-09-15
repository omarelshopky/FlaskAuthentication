from flask_sqlalchemy import SQLAlchemy
from app import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
