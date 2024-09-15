from flask import Blueprint, render_template, redirect, url_for
from flask_injector import inject
from app.services.products import ProductService
from app.forms.products.create_form import CreateForm
from app.forms.products.edit_form import EditForm


products = Blueprint("products", __name__)

@products.route("/")
@inject
def list_all(product_service: ProductService):
    return render_template("products/list.html", products=product_service.get_all())

@products.route("/create")
def create():
    return render_template("/products/create.html", form=CreateForm())

@products.route("/", methods=["POST"])
@inject
def store(product_service: ProductService):
    create_form = CreateForm()

    if create_form.validate_on_submit():
        product_service.create(
            name=create_form.name.data,
            price=create_form.price.data
        )

        return redirect(url_for("products.list_all"))

    return render_template("/products/create.html", form=create_form)

@products.route("/<public_id>")
@inject
def view(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return redirect(url_for("products.list_all"))

    return render_template("products/view.html", product=product)

@products.route("/<public_id>/edit")
@inject
def edit(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return redirect(url_for("products.list_all"))

    return render_template("products/edit.html", form=EditForm(), product=product)

@products.route("/<public_id>", methods=["POST"])
@inject
def update(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if not product:
        return redirect(url_for("products.list_all"))

    edit_form = EditForm()

    if edit_form.validate_on_submit():
        product_service.update(
            product,
            edit_form.name.data,
            edit_form.price.data
        )

        return redirect(url_for("products.list_all"))

    return render_template("products/view.html", product=product)

@products.route("/<public_id>", methods=["DELETE"])
@inject
def delete(product_service: ProductService, public_id):
    product = product_service.get_by_public_id(public_id)

    if product:
        product_service.delete(product)

    return redirect(url_for("products.list"))