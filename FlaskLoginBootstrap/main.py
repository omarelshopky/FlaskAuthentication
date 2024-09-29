from app import create_app, login_manager
from flask_injector import FlaskInjector, singleton
from app.core.sqlalchemy_base_model import SQLAlchemyBaseModel
from app.services.products import ProductService
from app.services.user import UserService


app = create_app()

# Configure and enable Dependency Injection
def configure(binder):
    binder.bind(ProductService, to=ProductService, scope=singleton)
    binder.bind(UserService, to=UserService, scope=singleton)

FlaskInjector(app=app, modules=[configure])

@login_manager.user_loader
def load_user(user_id):
    return UserService.get_by_id(user_id)

if __name__ == '__main__':
    if app.config["CREATE_DATABASE_IF_NOT_FOUND"] and app.config["DATABASE_TYPE"] == "sqlalchemy":
        with app.app_context():
            SQLAlchemyBaseModel.db.create_all()

    app.run()