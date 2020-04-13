from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_bootstrap import Bootstrap
import sqlite3
import smtplib
import db_methods as dbm


app = Flask(__name__)
app.secret_key = 'super secret key'
Bootstrap(app)
#render para ingresar al index
@app.route('/')
def index():
    return render_template('index.html')

#get and post del login
@app.route('/login',  methods=['GET', 'POST'])
def login():

    #Si existe un post se conecta a la base de datos y busca el usuario y la contraseña
    if request.method == 'POST':


        #toma de los parametros 
        Id = request.form['username']
        contra = request.form['inputPassword']

        #Se llama el metodo para validar el login
        resu = dbm.selectlogin(Id,contra)
        for row in resu:
            tipo = row [2]

        #se toma el nombre del usuario de la base de datos esto con el fin de mostrarlo en la pantalla de cada usuario
        rowsName = dbm.selectusername(Id)
        for row in rowsName:
            text = row[0]
        if resu and tipo == 'Admin':
            return redirect( url_for('.dashboard'))
        elif resu and tipo == 'Lead':
            return render_template('dashboard.html', name= text)
        elif resu and tipo == 'Usuario':
            return render_template('usuario.html', name= text)
        
        else:
            flash("Datos incorrectos")
    return render_template('login.html')

#Metodo get and post del registrar para poder ingresar al sistema
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    #si hay una accion post toma los datos del html
    if request.method == 'POST':

        #captura de los datos del html
        inName = request.form['inputUsuario']
        inPass =  request.form['inputPassword']
        inEmail = request.form['inputEmail']
        inAge = request.form['inputAge']
        iTipUsu = request.form['tipoUsu']
        inSecret = request.form["inputSecret"]
        parametros = [(inName, inPass, inEmail, inAge,iTipUsu)]
        
        
        #Se insertan los usuarios a la bd
        dbm.insertuser(parametros)

        #flash de información para que acceda al sistema
        flash("Su ID Usuario fue enviado a su correo")

        #conexion a bd para obtener el userid y asi poder enviarlo al correo registrado
        user = dbm.notify(str(inEmail))
        for row in user:
            text = row[0]
        conver = str(text)
       
        
        #Se envia un correo al usuario que se registre, se le enviará su USERID Unico y su contraseña
        conte = ("Este es su ID para ingresar al sistema "+conver+ " y su password " +inPass+"")
        mail = smtplib.SMTP('smtp.gmail.com', 587 )
        mail.ehlo()
        mail.starttls()
        mail.login('logintest91@gmail.com', 'Generacion1234')
        mail.sendmail('logintest91@gmail.com', ''+inEmail+'', conte)
        mail.close()
        
        #Inserta palabra de seguridad
        secret = [(conver,inSecret)]
        dbm.insertquestion(secret)

        return redirect('login')
    
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    test = dbm.selectusers()

    return render_template('dashboard.html', data = test, name = "Administrador")


    
if __name__ == '__main__':
    app.run(debug=True)