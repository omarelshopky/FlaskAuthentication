from flask import Flask, url_for
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # Create Flask Application
    app = Flask(__name__)

    # Load the Configuration
    app.config.from_object(Config)

    # Load Extensions
    db.init_app(app)
    Bootstrap(app)

    login_manager.init_app(app)
    login_manager.login_view = app.config["LOGIN_MANAGER_LOGIN_VIEW"]

    # Register Global variables for templates
    @app.context_processor
    def template_global_variables():
        return {
            'url_for': url_for,
        }

    # Register Blueprints
    from app.routes.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from app.routes.products import products as products_blueprint
    app.register_blueprint(products_blueprint, url_prefix="/products")

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from app.routes.user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")

    return app