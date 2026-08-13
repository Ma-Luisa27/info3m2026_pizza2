from flask import render_template, request, redirect, flash
from models import Usuario
from utils import db
from flask import Blueprint

bp_pizza = Blueprint("pizza", __name__, template_folder='templates')

@bp_pizza.route('/recovery')
def recovery():
	return render_template('pizza_recovery.html')