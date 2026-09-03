from flask import Blueprint, render_template, request, redirect, url_for

from models import Pedido, Pizza, Usuario
from utils import db


bp_pedido = Blueprint("pedido", __name__, template_folder="templates")


@bp_pedido.route("/get")
def get():
    pedidos = Pedido.query.all()
    return render_template("pedido_get.html", pedidos=pedidos)


@bp_pedido.route("/add", methods=["GET", "POST"])
def add():
    pizzas = Pizza.query.all()
    usuarios = Usuario.query.all()

    if request.method == "GET":
        return render_template("pedido_add.html", pizzas=pizzas, usuarios=usuarios)

    pizza_id = request.form.get("pizza_id", type=int)
    pizzas_selecionadas = request.form.getlist("pizzas")

    if pizza_id and not pizzas_selecionadas and not request.form.get("usuario_id"):
        return render_template("pedido_add.html", pizzas=pizzas, usuarios=usuarios, selected_pizza_id=pizza_id)

    pedido = Pedido()
    usuario_id = request.form.get("usuario_id", type=int)
    pedido.usuario = Usuario.query.get_or_404(usuario_id)

    for pizza in pizzas:
        if str(pizza.id) in pizzas_selecionadas:
            pedido.pizzas.append(pizza)

    db.session.add(pedido)
    db.session.commit()
    return redirect(url_for(".get"))


@bp_pedido.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    pedido = Pedido.query.get_or_404(id)
    pizzas = Pizza.query.all()
    usuarios = Usuario.query.all()

    if request.method == "GET":
        return render_template("pedido_update.html", pedido=pedido, pizzas=pizzas, usuarios=usuarios)

    pizzas_selecionadas = request.form.getlist("pizzas")
    pedido.pizzas = []
    for pizza in pizzas:
        if str(pizza.id) in pizzas_selecionadas:
            pedido.pizzas.append(pizza)

    usuario_id = request.form.get("usuario_id", type=int)
    pedido.usuario = Usuario.query.get_or_404(usuario_id)

    db.session.commit()
    return redirect(url_for(".get"))


@bp_pedido.route("/delete/<int:id>")
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for(".get"))

