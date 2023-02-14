from regtel.extensions import Flask,SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.sqlite"
db.init_app(app)

try:
    from regtel.models import *
except:
    print('\n-------------------------\n[erro ao importar model]\n-------------------------\n')

with app.app_context():
    db.create_all()

from regtel.routes import *