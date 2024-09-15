from flask import Blueprint, jsonify, request
from flask_injector import inject
from app.services.products import ProductService
from app.controllers.utils import verify_missing_data


products = Blueprint("products", __name__)

@products.route("/", methods=["POST"])
@inject
def list_all(product_service: ProductService):
    products = [product.to_dict() for product in product_service.get_all()]

    return jsonify(products)

@products.route("/create", methods=["POST"])
@inject
def create(product_service: ProductService):
    # get JSON data from request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Invalid JSON format"}), 400

    # verify JSON data
    missing_data = verify_missing_data(data, keys_to_verify=["name", "price"])
    if len(missing_data) > 0:
        return jsonify({
            "msg": "Missing " + ", ".join(missing_data)
        }), 400

    status = product_service.create(name=data["name"], price=data["price"])

    if not status:
        return jsonify({"msg": "Another product is already created with the same name"})

    return jsonify({"msg": "Product created successfully"})

@products.route("/<public_id>", methods=["POST"])
@inject
def view(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return jsonify({"msg": "Product not found"}), 400

    return jsonify(product.to_dict())

@products.route("/<public_id>/edit", methods=["POST"])
@inject
def edit(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return jsonify({"msg": "Product not found"}), 400

    # get JSON data from request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"msg": "Invalid JSON format"}), 400

    # verify JSON data
    missing_data = verify_missing_data(data, keys_to_verify=["name", "price"])
    if len(missing_data) > 0:
        return jsonify({
            "msg": "Missing " + ", ".join(missing_data)
        }), 400

    edited_product = product_service.update(product, data["name"], data["price"])

    return jsonify(edited_product.to_dict())

@products.route("/<public_id>", methods=["DELETE"])
@inject
def delete(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return jsonify({"msg": "Product not found"}), 400

    product_service.delete(product)

    return jsonify({"msg": "Product deleted successfully"})