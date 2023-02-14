from regtel import db

class Registo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    funcao = db.Column(db.String(50))
    entidade = db.Column(db.String(50))
    numero = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(50), unique=True)
    data_registo = db.Column(db.Date)
