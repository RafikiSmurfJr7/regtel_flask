from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

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



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'