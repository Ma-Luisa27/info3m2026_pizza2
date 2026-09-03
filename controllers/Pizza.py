from flask import render_template, request, redirect, url_for
from models import Pizza
from utils import db, lm
from flask import Blueprint
from flask_login import login_required

bp_pizza = Blueprint("pizza", __name__, template_folder='templates')

@bp_pizza.route('/get')
def get():
	pizzas = Pizza.query.all()
	return render_template('pizza_get.html', pizzas=pizzas)

@bp_pizza.route('/add', methods=['GET', 'POST'])
@login_required
def add():
	if request.method == 'GET':
		return render_template('pizza_add.html')

	pizza = Pizza(
		request.form.get('sabor'),
		float(request.form.get('preco')),
		request.form.get('imagem')
	)
	db.session.add(pizza)
	db.session.commit()
	return redirect(url_for('.get'))

@bp_pizza.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
	pizza = Pizza.query.get_or_404(id)
	if request.method == 'GET':
		return render_template('pizza_update.html', pizza=pizza)

	pizza.sabor = request.form.get('sabor')
	pizza.preco = float(request.form.get('preco'))
	pizza.imagem = request.form.get('imagem')
	db.session.commit()
	return redirect(url_for('.get'))

@bp_pizza.route('/delete/<int:id>')
@login_required
def delete(id):
	pizza = Pizza.query.get_or_404(id)
	db.session.delete(pizza)
	db.session.commit()
	return redirect(url_for('.get'))