from flask import Flask, url_for, make_response, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


db = SQLAlchemy()

def create_app():
    # Create Flask Application
    app = Flask(__name__)

    # Load the Configuration
    app.config.from_object(Config)

    # Load Extensions
    db.init_app(app)
    JWTManager(app)

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"] # [count] [per|/] [n (optional)] [second|minute|hour|day|month|year][s]
    )

    # Register Global variables for templates
    @app.context_processor
    def template_global_variables():
        return {
            'url_for': url_for,
        }

    # Change hit rate limit response message
    @app.errorhandler(429)
    def rate_limit_handler(e):
        return make_response(jsonify(error="rate limit exceeded") , 429)

    # Register Blueprints
    from app.routes.products import products as products_blueprint
    app.register_blueprint(products_blueprint, url_prefix="/products")

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    limiter.limit("10/hour;5/minute;1/second")(auth_blueprint)

    from app.routes.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")

    return app