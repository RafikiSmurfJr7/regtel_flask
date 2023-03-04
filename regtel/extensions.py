from flask_login import LoginManager
from regtel.models import db, User
from werkzeug.security import generate_password_hash


def make_admin():
    try:
        admin = User.query.filter_by(id=1).first()
        print(admin.id)
    except AttributeError:
        user = User(
            username='administrator',
            email='admin@mail.com',
            password=generate_password_hash('administrator',method='sha256')
        )
        db.session.add(user)
        db.session.commit()


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def init_app(app):
    db.init_app(app)
    login_manager.init_app(app)