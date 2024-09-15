from app import create_app, db
from flask_injector import FlaskInjector, singleton
from app.services.products import ProductService
from app.services.user import UserService


app = create_app()

# Configure and enable Dependency Injection
def configure(binder):
    binder.bind(ProductService, to=ProductService(db), scope=singleton)
    binder.bind(UserService, to=UserService(db), scope=singleton)

FlaskInjector(app=app, modules=[configure])

if __name__ == '__main__':
    if app.config["CREATE_DATABASE_IF_NOT_FOUND"]:
        with app.app_context():
            db.create_all()

    app.run()