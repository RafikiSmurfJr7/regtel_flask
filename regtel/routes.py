from regtel import app, db
from regtel.extensions import *
from regtel.models import Registo
from datetime import date

@app.route("/", methods=['GET', 'POST'])
def index():


    if request.method == 'GET':

        registo = db.session.execute(db.select(Registo).order_by(Registo.data_registo)).scalars()


        return render_template('home.html' ,data=registo)
    
    elif request.method == 'POST':


        registo = Registo(
            nome = request.form["nome"],
            funcao = request.form["funcao"],
            entidade = request.form["entidade"],
            numero = request.form["nTelPessoal"],
            email = request.form["email"],
            data_registo = date.today()
        )

        db.session.add(registo)
        db.session.commit()


        return redirect("/")