from flask import Flask
from regtel.config import Config
from regtel.extensions import db,init_app,login_manager
from flask_login import LoginManager


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"

    db.init_app(app)
    login_manager.init_app(app)
    init_app(app)


    

    from . import routes
    app.register_blueprint(routes.bp)

    return app


def create_database(app):
    with app.app_context():
        db.create_all()


#try:
#    from regtel.models import *
#except:
#    print('\n-------------------------\n[erro ao importar model]\n-------------------------\n')
#
#with app.app_context():
#    db.create_all()


    