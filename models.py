from utils import db

class Usuario(db.Model):
    __tablename__= "usuario"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):
        return "<Usuario {}>".format(self.nome)

class Pizza(db.Model):
    __tablename__= "pizza"
    id = db.Column(db.Integer, primary_key = True)
    sabor = db.Column(db.String(100))
    preco = db.Column(db.Float)
    pedidos = db.relationship("Pedido", secondary="pizza_pedido", back_populates="pizzas")

    def __init__(self, sabor, preco):
        self.sabor = sabor
        self.preco = preco
    
    def __repr__(self):
        return "<Pizza {}>".format(self.sabor)

class Pedido(db.Model):
    __tablename__ = "pedido"
    id = db.Column(db.Integer, primary_key=True)
    pizzas = db.relationship("Pizza", secondary="pizza_pedido", back_populates="pedidos")

    def __repr__(self):
        return "<Pedido {}>".format(self.id)

class PizzaPedido(db.Model):
    __tablename__ = "pizza_pedido"
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedido.id"), primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"), primary_key=True)