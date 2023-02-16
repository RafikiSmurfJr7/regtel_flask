from regtel import app, db
from regtel.extensions import *
from regtel.models import Registo
from datetime import date, datetime

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        registo = db.session.execute(db.select(Registo).order_by(Registo.data_registo)).scalars()

        return render_template('home.html' ,data=registo)
    
    elif request.method == 'POST':

        if request.form["dataNasc"] != '':
                
            data_nasc = datetime.strptime(request.form["dataNasc"],'%Y-%m-%d')

        else:

            data_nasc = None

        registo = Registo(
            nome = request.form["nome"],
            email = request.form["email"],
            data_nasc = data_nasc,
            numero = request.form["nTelPessoal"],
            funcao = request.form["funcao"],
            entidade = request.form["entidade"],
            data_registo = date.today()
        )

        db.session.add(registo)
        db.session.commit()


        return redirect("/")
    

@app.route("/delete/<int:id>")
def delete_record(id):
    
    record = db.one_or_404(db.select(Registo).filter_by(id=id))
    db.session.delete(record)
    db.session.commit()

    return redirect("/")


@app.route("/profile/<int:id>")
def profile(id):
    
    record = db.one_or_404(db.select(Registo).filter_by(id=id))
    
    return render_template("profile.html" ,data=record)

@app.route("/profile/edit/about/<int:id>", methods=['POST'])
def profile_edit_about(id):
        
        descricao = request.form['sobre'].replace('\n','<br>')

        record = db.get_or_404(Registo, id)
        record.descricao = descricao
        db.session.commit()

        return redirect("/profile/" + str(id))


@app.route("/profile/edit/data/<int:id>", methods=['POST'])
def profile_edit_data(id):
        
    record = db.get_or_404(Registo, id)

    if request.form["dataNasc"] != '':
        data_nasc =  record.data_nasc = datetime.strptime(request.form["dataNasc"],'%Y-%m-%d')
    else:    
        data_nasc = None
    
    record.nome = request.form['nome']
    record.data_nasc = data_nasc
    record.email = request.form['email']
    record.numero = request.form['telemovel']
    record.entidade = request.form['entidade']
    record.funcao = request.form['funcao']
    
    
    db.session.commit()


    return redirect("/profile/"+ str(id))

@app.route('/profile/delete/about/<int:id>')
def profile_delete_about(id):
    
    record = db.get_or_404(Registo, id)
    record.descricao = None
    db.session.commit()
    return redirect('/profile/' + str(id))