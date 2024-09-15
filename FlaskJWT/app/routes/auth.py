from flask import Blueprint, request, jsonify
from flask_injector import inject
from app.services.user import UserService
from app.controllers.utils import check_password_strength, verify_missing_data

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
@inject
def login(user_service: UserService):
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Invalid JSON format"}), 400
    
    # verify JSON data
    missing_data = verify_missing_data(data, keys_to_verify=["username", "password"])
    if len(missing_data) > 0:
        return jsonify({
            "msg": "Missing " + ", ".join(missing_data)
        }), 400

    access_token = user_service.login(data["username"], data["password"])

    # user doesn't exist
    if not access_token:
        return jsonify({"msg": "Incorrect username or password"}), 400

    return jsonify(access_token=access_token)

@auth.route("/signup", methods=["POST"])
@inject
def signup(user_service: UserService):
    """handles the user registration process"""
    # get JSON data from request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Invalid JSON format"}), 400

    # verify JSON data
    missing_data = verify_missing_data(data, keys_to_verify=["name", "username", "password"])
    if len(missing_data) > 0:
        return jsonify({
            "msg": "Missing " + ", ".join(missing_data)
        }), 400

    # check if user exists
    if user_service.get_by_username(username=data["username"]) is not None:
        return jsonify({
            "msg": "User already exists"
        }), 400

    # check password strength
    if not check_password_strength(data["password"]):
        return jsonify({
            "msg": "Weak password"
        }), 400

    user_service.signup(data["name"], data["username"], data["password"])

    return jsonify({"msg": "User registered successfully"})