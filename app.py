from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'

mysql = MySQL(app)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/area")
def area():
    return render_template("area.html")

@app.route("/register/",methods = ["GET","POST"])
def registrati():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'nome' in request.form and 'cognome' in request.form and 'v_password' in request.form:
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        username = request.form.get('username')
        password = request.form.get('password')
        v_password = request.form.get('v_password')
        cursor = mysql.connection.cursor()
        query ="INSERT INTO users VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(nome,cognome,username,password))
        mysql.connection.commit()
        return redirect(url_for('area'))

app.run(debug=True)
