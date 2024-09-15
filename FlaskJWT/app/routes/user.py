from flask import Blueprint, render_template
from flask_jwt_extended import current_user, jwt_required

user = Blueprint("user", __name__)

@user.route("/profile", methods=["POST"])
@jwt_required()
def profile():
    return f"Hello to the protected area, your username is {current_user.username}"
