from flask import Flask ,render_template ,request ,redirect
from db import DataBaseConnection as dbConn
from configdb import dbdata
from datetime import date


app = Flask(__name__)

db = dbConn(dbdata['username'],dbdata['password'],dbdata['host'],dbdata['database'])


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        query = "SELECT Registos.id as 'ID', Contatos.name as 'Nome', Funcao.name as 'Funcao', Entidades.name as 'Entidades', Contatos.contatoTelefonico as 'NumTele', Contatos.email as 'Email', Registos.data as 'Data' FROM Registos INNER JOIN Contatos on Registos.contatosId = Contatos.id INNER JOIN Entidades ON Contatos.entidadesId = Entidades.id INNER JOIN Funcao ON Contatos.funcaoId = Funcao.id"

        dataQ = db.makeQuery(query)
        
        return render_template("home.html" ,data=dataQ)
    
    elif request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        data = request.form['date']
        nPessoal = request.form['nTelPessoal']
        nTrab = request.form['nTelTrab']
        funcao = request.form['funcao']
        entidade = request.form['entidade']

        dataHoje = date.today()

        query = (
            """
            INSERT INTO Funcao(Funcao.name) VALUES ('{}');
            
            INSERT INTO Entidades (Entidades.name) VALUES ('{}');
            
            INSERT INTO Contatos(Contatos.name,Contatos.contatoTelefonico,Contatos.email,Contatos.entidadesId,Contatos.funcaoId)
            VALUES ('{}', '{}','{}',(SELECT id FROM Entidades WHERE Entidades.name LIKE '{}'),(SELECT id FROM Funcao WHERE Funcao.name LIKE '{}'));
            
            INSERT INTO Registos (Registos.utilizadoresId,Registos.contatosId,Registos.data) 
            VALUES (1, (SELECT Contatos.id FROM Contatos WHERE Contatos.email LIKE '{}'), '{}')
            
            """).format(funcao,entidade,name,nPessoal,email,entidade,funcao,email,dataHoje)
        
        db.makeQuery(query)


        return redirect("/")
    else:
        return redirect("/")