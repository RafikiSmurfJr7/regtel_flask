from regtel import db

class Registo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    data_nasc = db.Column(db.Date)
    email = db.Column(db.String(50))
    funcao = db.Column(db.String(50))
    entidade = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100))
    data_registo = db.Column(db.Date)

