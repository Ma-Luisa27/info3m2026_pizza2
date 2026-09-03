from flask import render_template, request, redirect, url_for, flash
from models import Usuario
from utils import db
from flask import Blueprint

bp_usuario = Blueprint("usuario", __name__, template_folder='templates')

@bp_usuario.route('/get')
def get():
	usuarios = Usuario.query.all()
	return render_template('usuario_get.html', usuarios=usuarios)

@bp_usuario.route('/add', methods=['GET', 'POST'])
def add():
	if request.method=="GET":
		return render_template('usuario_add.html')
	elif request.method=="POST":
		nome = request.form.get('nome')
		email = request.form.get('email')
		senha = request.form.get('senha')
		u = Usuario(nome, email, senha)
		db.session.add(u)
		db.session.commit()
		return redirect(url_for('.get'))

@bp_usuario.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	u = Usuario.query.get(id)
	if request.method=="GET":
		return render_template('usuario_update.html', u=u)
	elif request.method=="POST":
		u.nome = request.form.get('nome')
		u.email = request.form.get('email')
		u.senha = request.form.get('senha')
		db.session.add(u)
		db.session.commit()
		return redirect(url_for('.get'))

@bp_usuario.route('/delete/<int:id>')
def delete(id):
	u = Usuario.query.get(id)
	db.session.delete(u)
	db.session.commit()
	return redirect(url_for('.get'))