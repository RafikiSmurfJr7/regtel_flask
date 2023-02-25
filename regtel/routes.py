from flask import Blueprint, render_template, redirect, url_for, request, flash,escape
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from regtel.models import User,Registo
from regtel.extensions import db,login_manager
from datetime import date, datetime


bp = Blueprint('registo', __name__)


@login_manager.unauthorized_handler
def unauthorized():
    flash('Tem de fazer o login para aceder','warning')
    return redirect(url_for('registo.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('registo.index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
    
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('registo.index'))
        else:
            flash('Nome de utilizador ou password invalida','danger')
    return render_template('login.html')



@bp.route('/logout')
@login_required
def logout():
    msg = 'Adeus ' + current_user.username
    flash(msg, 'primary')
    logout_user()
    return redirect(url_for('registo.login'))


@bp.route("/", methods=['GET', 'POST'])
@login_required
def index():
    
    if request.method == 'GET':

        registo = db.session.execute(db.select(Registo).order_by(Registo.data_registo)).scalars()

        if current_user.is_authenticated:
            msg = 'Olá ' + current_user.username
            flash(msg, 'primary')

        return render_template('home.html' ,data=registo)

    elif request.method == 'POST':

        
        data_nasc = datetime.strptime(request.form["dataNasc"],'%Y-%m-%d') if request.form["dataNasc"] != '' else  None
        
        try:
            visibilidade = 'private' if request.form["regPrivado"] == 'on' else None    
        except:
            visibilidade = None

        registo = Registo(
            nome = request.form["nome"],
            email = request.form["email"],
            data_nasc = data_nasc,
            numero = request.form["nTelPessoal"],
            funcao = request.form["funcao"],
            entidade = request.form["entidade"],
            data_registo = date.today(),
            registado_por = current_user.get_id(),
            visibilidade = visibilidade
        )

        try:
            db.session.add(registo)
            db.session.commit()

        except db.exc.IntegrityError:

            flash('Erro de integridade [Tentou inserir dados repetidos]','danger')
            
            return redirect(url_for('registo.index'))
        

        flash('Registo inserido com sucesso','success')
        return redirect(url_for('registo.index'))
    

@bp.route("/delete/<int:id>")
@login_required
def delete_record(id):
    
    record = db.one_or_404(db.select(Registo).filter_by(id=id))
    db.session.delete(record)
    db.session.commit()

    flash('Registo eliminado','danger')
    return redirect("/")


@bp.route("/profile/<int:id>")
@login_required
def profile(id):
    
    record = db.one_or_404(db.select(Registo).filter_by(id=id))
    
    return render_template("profile.html" ,data=record)


@bp.route("/profile/edit/data/<int:id>", methods=['POST'])
@login_required
def profile_edit_data(id):
        
    record = db.get_or_404(Registo, id)

    
    data_nasc =  record.data_nasc = datetime.strptime(request.form["dataNasc"],'%Y-%m-%d') if request.form["dataNasc"] != '' else None
    
    try:
        visibilidade = 'private' if request.form["regPrivado"] == 'on' else 'public'    
    except:
        visibilidade = 'public'


    record.nome = request.form['nome']
    record.data_nasc = data_nasc
    record.email = request.form['email']
    record.numero = request.form['telemovel']
    record.entidade = request.form['entidade']
    record.funcao = request.form['funcao']
    record.visibilidade = visibilidade

    try:
        db.session.commit()
    except db.exc.IntegrityError:
        flash('Esse contato já está registado','danger')      
        return redirect('/profile/' +  str(id))
        
    flash(escape('Dados alterados com sucesso!'),'success')
    return redirect("/profile/"+ str(id))



@bp.route("/profile/edit/about/<int:id>", methods=['POST'])
@login_required
def profile_edit_about(id):
        
        descricao = request.form['sobre'].replace('\n','<br>')

        record = db.get_or_404(Registo, id)
        record.descricao = descricao
        db.session.commit()


        flash('Alteração guardada com sucesso!','success')
        return redirect("/profile/" + str(id))



@bp.route('/profile/delete/about/<int:id>')
@login_required
def profile_delete_about(id):
    
    record = db.get_or_404(Registo, id)
    record.descricao = None
    db.session.commit()

    flash('Eliminado com sucesso!','warning')
    return redirect('/profile/' + str(id))


@bp.route('/admin', methods=['GET','POST'])
@login_required
def admin():

    if request.method == 'POST':
        
        username = request.form["username"]
        email = request.form['email']
        password = request.form['password']
        conf_password = request.form['confPassword']

        if password == conf_password:

            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password,method='sha256')
            )

            try:

                db.session.add(user)
                db.session.commit()
            except db.exc.IntegrityError:
                flash('Email ou nome de utilizador já se encontram registados!','danger')
                return redirect(url_for('registo.admin'))
            
            flash('Utilizador registado com sucesso!','success')
            return redirect(url_for('registo.admin'))

        else:
            flash('Passwords não combinam!','danger')
            
            return redirect(url_for('registo.admin'))

    else:
    
        users = db.session.execute(db.select(User).order_by(User.id)).scalars()

        return render_template('admin.html', data=users)
    
    
@bp.route("/admin/delete/<int:id>")
@login_required
def delete_user(id):
    
    record = db.one_or_404(db.select(User).filter_by(id=id))
    db.session.delete(record)
    db.session.commit()

    flash('Utilizador eliminado','warning')
    return redirect(url_for('registo.admin'))

