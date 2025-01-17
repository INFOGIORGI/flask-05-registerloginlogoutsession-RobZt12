from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)


app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'

mysql = MySQL(app)
app.secret_key = "segereto"
@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("login.html")

@app.route("/area")
def area():
    return render_template("area.html")

@app.route("/register/",methods = ["GET","POST"])
def registrati():
    if request.method == "GET":
        return render_template("register.html")
    
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    username = request.form.get('username')
    password = request.form.get('password')
    v_password = request.form.get('v_password')


    for item in [nome, cognome, username, password, v_password]:
        if item == "":
            flash("Tutti i campi hannu a èssiri cumpilati")
            return redirect("/register")
        
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query,(username,))
    result = cursor.fetchall()
    if result:
        flash("Username già prisenti, mo capisti?")
        return redirect("/register")


    cursor = mysql.connection.cursor()
    query ="INSERT INTO users VALUES(%s,%s,%s,%s)"
    cursor.execute(query,(username,generate_password_hash(password),nome,cognome))
    """La flash() prende una serie di messaggi
    e li inserisce all'interno di un vettore"""
    mysql.connection.commit()
    return redirect(url_for('area'))
        
      
            
app.run(debug=True)
