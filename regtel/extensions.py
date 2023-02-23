from flask_login import LoginManager
from regtel.models import db, User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def init_app(app):
    login_manager.init_app(app)