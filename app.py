"""
Application file
"""

from flask import Flask, request, render_template
from views.products import products_app  # аналог подключения роутера в FastAPI

app = Flask(__name__)  # создание приложения (класса от Flask)

app.config.update(ENV="development", SECRET_KEY="fgdfgfdbdfgbdfgghyhrrwe")

app.register_blueprint(products_app, url_prefix="/products")


@app.route("/")  # обычная ввью функция, которая выведет дынные
def hello_world():
    """
    hello_world func
    :return:
    """
    print_request()
    # return "<h1>Hello, World!<h1>"
    return render_template("index.html")
    # return render_template("base.html")


def print_request():
    """
    print_request func
    :return:
    """
    # различные свойства данного запроса
    print("request", request)
    print("request.method", request.method)
    print("request.path", request.path)


@app.route("/hello/")  # "/hello/" и "/hello" - два разных маршрута
@app.route("/hello/<name>/")  # можем накрутить два декоратора (два маршрута)
def hello_view(name: str = None):
    """
    hello_view func
    :return:
    """
    print_request()
    if name is None:
        name = request.args.get(
            "name", ""
        )  # если передано несколько имен - берем первое в запросе
    name = name.strip()
    if not name:
        name = "world"

    # names = request.args.getlist("name")  # поддержка нескольких ключей
    # print(request.args)

    # print("request", request)  # переменная request доступна только внутри вью-функции
    # (нельзя обратиться к "запросу вне запроса")

    return {"message": f"Hello {name}"}  # Flask понимает, что это json и возвращает его


@app.route("/items/<int:item_id>/")
def get_item(item_id: int):
    """
    get_item func
    :return:
    """
    return {
        "item": {"id": item_id},
    }


@app.route("/items/<item_id>/")
def get_item_string(item_id: str):
    """
    get_item_string func
    :return:
    """
    return {
        "item_id": {"id": item_id.upper()},
    }


# @app.route("/hello/<name>/")
# def hello_name(name: str):
#     return {"message": f"Hello {name}"}

# NEVER
# print("request", request)  # (нельзя обратиться к "запросу вне запроса")
if __name__ == "__main__":
    # app.run(host="0.0.0.0", debug=True)
    app.run(debug=True)
# это первый тип запуска приложения
# второй - через терминал; flask --app main run
