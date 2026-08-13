from flask import render_template, request, redirect, url_for, flash
from models import Usuario
from utils import db
from flask import Blueprint

bp_usuario = Blueprint("usuario", __name__, template_folder='templates')

@bp_usuario.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuario_recovery.html', usuarios=usuarios)

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
		return redirect(url_for('.recovery'))

