from flask_sqlalchemy import SQLAlchemy
from app.core.base_model import BaseModel

database = SQLAlchemy()

class SQLAlchemyBaseModel(BaseModel, database.Model):
    __metaclass__ = database.Model
    __abstract__ = True
    _db = database

    @classmethod
    @property
    def db(cls):
        return cls._db

    @classmethod
    def select(cls, attributes, only_one=False):
        result = cls.query.filter_by(**attributes)

        if only_one:
            return result.first()

        return result

    @classmethod
    def select_all(cls):
        return cls.query.all()

    @classmethod
    def select_by_id(cls, id):
        return cls.query.get(int(id))

    def insert(self):
        self.db.session.add(self)
        self.db.session.commit()

    def update(self):
        self.db.session.commit()

    def delete(self):
        self.db.session.delete(self)
        self.db.session.commit()