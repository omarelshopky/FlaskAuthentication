from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
import uuid
from app.models.user import User


class UserService:
    @classmethod
    def get_by_id(cls, id):
        return User.select_by_id(id)

    def get_by_username(self, username):
        return User.select({"username": username}, only_one=True)

    def login(self, username, password):
        user = self.get_by_username(username)

        if not user or not check_password_hash(user.password, password):
            return False
    
        login_user(user)

        return True

    def signup(self, name, username, password):
        user = User(
            public_id=str(uuid.uuid4()),
            name=name,
            username=username,
            password=generate_password_hash(password)
        )

        user.insert()

    def logout(self):
        logout_user()


