from pymongo import MongoClient, errors as pymongo_errors
from bson import ObjectId
from app.core.base_model import BaseModel
from config import Config


try:
    client = MongoClient(Config.MONGODB_DATABASE_URI)
except pymongo_errors.ConfigurationError:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
    sys.exit(1)

class MongoBaseModel(BaseModel):
    collection_name = None
    _db = client[Config.MONGODB_DATABASE_NAME]

    @classmethod
    @property
    def db(cls):
        return cls._db

    @classmethod
    def get_collection(cls):
        if cls.collection_name is None:
            raise ValueError("You must define a collection_name for MongoBaseModel")
        return cls.db[cls.collection_name]

    @classmethod
    def from_dict(cls, data):
        """Convert a dictionary to an instance of the model class."""
        instance = cls()
        for key, value in data.items():
            setattr(instance, key, value)
        return instance

    @classmethod
    def select(cls, attributes, only_one=False):
        collection = cls.get_collection()

        if only_one:
            document = collection.find_one(attributes)
            return cls.from_dict(document) if document else None

        return [cls.from_dict(document) for document in collection.find(attributes)]

    @classmethod
    def select_all(cls):
        return [cls.from_dict(document) for document in cls.get_collection().find()]

    @classmethod
    def select_by_id(cls, id):
        document = cls.get_collection().find_one({"_id": ObjectId(id)})
        return cls.from_dict(document) if document else None

    def insert(self):
        self.get_collection().insert_one(self.to_dict())

    def update(self):
        self.get_collection().update_one({"_id": self._id}, {"$set": self.to_dict()})

    def delete(self):
        self.get_collection().delete_one({"_id": self._id})