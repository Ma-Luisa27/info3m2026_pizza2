from flask import Blueprint, render_template, request, redirect, url_for

from models import Pedido, Pizza
from utils import db


bp_pedido = Blueprint("pedido", __name__, template_folder="templates")


@bp_pedido.route("/get")
def get():
    pedidos = Pedido.query.all()
    return render_template("pedido_get.html", pedidos=pedidos)


@bp_pedido.route("/add", methods=["GET", "POST"])
def add():
    pizzas = Pizza.query.all()

    if request.method == "GET":
        selected_pizza_id = request.args.get("pizza_id", type=int)
        return render_template("pedido_add.html", pizzas=pizzas, selected_pizza_id=selected_pizza_id)

    pedido = Pedido()
    pedido.pizzas = _pizzas_from_form(pizzas)
    db.session.add(pedido)
    db.session.commit()
    return redirect(url_for(".get"))


@bp_pedido.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    pedido = Pedido.query.get_or_404(id)
    pizzas = Pizza.query.all()

    if request.method == "GET":
        return render_template("pedido_update.html", pedido=pedido, pizzas=pizzas)

    pedido.pizzas = _pizzas_from_form(pizzas)
    db.session.commit()
    return redirect(url_for(".get"))


@bp_pedido.route("/delete/<int:id>")
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for(".get"))


def _pizzas_from_form(pizzas):
    pizza_ids = {int(pizza_id) for pizza_id in request.form.getlist("pizzas")}
    return [pizza for pizza in pizzas if pizza.id in pizza_ids]