from flask import Flask ,render_template ,request ,redirect
from db import DataBaseConnection as dbConn
from configdb import dbdata


app = Flask(__name__)

db = dbConn(dbdata['username'],dbdata['password'],dbdata['host'],dbdata['database'])


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        query = "SELECT Registos.id as 'ID', Contatos.name as 'Nome', Funcao.name as 'Funcao', Entidades.name as 'Entidades', Contatos.contatoTelefonico as 'NumTele', Contatos.email as 'Email', Registos.data as 'Data' FROM Registos INNER JOIN Contatos on Registos.contatosId = Contatos.id INNER JOIN Entidades ON Contatos.entidadesId = Entidades.id INNER JOIN FuncaoEntidades ON Entidades.id = FuncaoEntidades.entidadesId INNER JOIN Funcao ON FuncaoEntidades.funcaoId = Funcao.id"

        dataQ = db.makeQuery(query)
        
        return render_template("home.html" ,data=dataQ)
    
    elif request.method == 'POST':
        pass

    else:
        return redirect("/")