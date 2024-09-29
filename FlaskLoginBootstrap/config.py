import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
    CREATE_DATABASE_IF_NOT_FOUND = os.getenv("CREATE_DATABASE_IF_NOT_FOUND", True)
    DATABASE_TYPE = os.getenv("DATABASE_TYPE", "sqlalchemy")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    MONGODB_DATABASE_URI = os.getenv("MONGODB_DATABASE_URI")
    MONGODB_DATABASE_NAME = os.getenv("MONGODB_DATABASE_NAME")
    SECRET_KEY = os.getenv("SECRET_KEY")
    LOGIN_MANAGER_LOGIN_VIEW = os.getenv("LOGIN_MANAGER_LOGIN_VIEW", "auth.login")