"""
Products views
"""

# from main import app  - циклический импорт
from flask import Blueprint, render_template, request, redirect
from werkzeug.exceptions import NotFound

from views.forms.products import CreateProductForm

# print("__name__", __name__)
products_app = Blueprint("products_app", __name__)  # аналог APIRouter в FastAPI

PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


@products_app.route("/", endpoint="list")
def get_products():
    """
    get_products
    :return:
    """
    return render_template("products/list.html", products=PRODUCTS)
    # рендер темплита и передача продуктов в шаблон


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product(product_id: int):
    """
    get_product
    :param product_id:
    :return:
    """
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product {product_id} not found")
    return render_template(
        "/products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    """
    add_product
    :return:
    """
    form = CreateProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data
    # вынесли часть логики в форму (закоментированный блок выше - аналогично, но сложнее)

    print(product_name)

    return redirect('/')
