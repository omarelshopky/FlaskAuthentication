from abc import ABC, abstractmethod

class BaseModel:
    @classmethod
    @abstractmethod
    def select(cls, attributes, only_one=False):
        pass

    @classmethod
    @abstractmethod
    def select_all(cls):
        pass

    @classmethod
    @abstractmethod
    def select_by_id(cls, id):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
