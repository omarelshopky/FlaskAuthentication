from flask_sqlalchemy import SQLAlchemy
from flask_injector import inject
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import uuid
from app.models.user import User


class UserService:
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_by_id(self, id):
        return User.query.get(int(id))

    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def login(self, username, password):
        user = self.get_by_username(username)

        if not user or not check_password_hash(user.password, password):
            return None

        return create_access_token(identity=user.public_id)

    def signup(self, name, username, password):
        user = User(
            public_id=str(uuid.uuid4()),
            name=name,
            username=username,
            password=generate_password_hash(password)
        )
        self.db.session.add(user)
        self.db.session.commit()

    def logout(self):
        logout_user()


