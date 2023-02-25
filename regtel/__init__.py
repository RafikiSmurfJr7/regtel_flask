from flask import Flask
from regtel.config import Config
from regtel.extensions import db,init_app,login_manager


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)


    from . import routes
    app.register_blueprint(routes.bp)

    return app


def create_database(app):
    with app.app_context():
        db.create_all()



    