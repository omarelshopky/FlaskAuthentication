from app import create_app, db, jwt
from flask_injector import FlaskInjector, singleton
from app.services.products import ProductService
from app.services.user import UserService


app = create_app()

# Configure and enable Dependency Injection
def configure(binder):
    binder.bind(ProductService, to=ProductService(db), scope=singleton)
    binder.bind(UserService, to=UserService(db), scope=singleton)

FlaskInjector(app=app, modules=[configure])

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.public_id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    return UserService(db).get_by_public_id(jwt_data["public_id"])

if __name__ == '__main__':
    if app.config["CREATE_DATABASE_IF_NOT_FOUND"]:
        with app.app_context():
            db.create_all()

    app.run()