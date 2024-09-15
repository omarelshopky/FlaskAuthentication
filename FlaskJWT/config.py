import os
import datetime
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)
    CREATE_DATABASE_IF_NOT_FOUND = os.getenv("CREATE_DATABASE_IF_NOT_FOUND", True)
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///database.db")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES")))
    JWT_IDENTITY_CLAIM = os.getenv("JWT_IDENTITY_CLAIM")