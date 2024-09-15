from flask import Blueprint, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required

user = Blueprint("user", __name__)

@user.route("/profile", methods=["POST"])
@jwt_required()
def profile():
    return f"Hello to the protected area, your public id is {get_jwt_identity()}"
