from flask import render_template, request, redirect, flash
from models import Usuario
from utils import db
from flask import Blueprint

bp_usuario = Blueprint("usuario", __name__, template_folder='templates')

@bp_usuario.route('/recovery')
def recovery():
	usuarios = Usuario.query.all()
	return render_template('usuario_recovery.html', usuarios=usuarios)