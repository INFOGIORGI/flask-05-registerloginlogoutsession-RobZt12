from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)

app.secret_key ='miao'


app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_DB'] = 'w3schools'
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] ='ospite'

myslq = MySQL(app)

@app.route('/',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome','')
        cognome = request.form.get('cognome','')
        username = request.form.get('username','')
        password = request.form.get('password','')
        v_password = request.form.get('v_password','')
        if nome == '' or cognome == '' or username == '' or password =='' or v_password =='':
            flash('Inserire tutti i campi')
            return redirect (url_for('register'))
        else:
            if password != v_password:
                flash('Password non corrispondenti')
                return redirect (url_for('register'))        
            cursor = myslq.connection.cursor()
            query_u = 'SELECT username FROM users WHERE username = %s'
            cursor.execute(query_u,(username,))
            result = cursor.fetchall()
            if len(result) != 0:
                flash('Username gia esiste')
                return redirect (url_for('register'))
            query = 'INSERT INTO users VALUES(%s,%s,%s,%s)'
            cursor.execute(query,(username,generate_password_hash(password),nome,cognome))
            myslq.connection.commit()
            cursor.close()
            return redirect (url_for('login'))
    return render_template('register.html',titolo = 'Registrati')
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username','')
        password = request.form.get('password','')
        cursor = myslq.connection.cursor()
        query = 'SELECT password FROM users WHERE username = %s'
        cursor.execute(query,(username,))
        result = cursor.fetchall()
        if len(result) == 0:
            flash('Utente non esistente')
            return redirect (url_for('register'))
        else:
            password_h = result[0][0]
            if check_password_hash(password_h,password):
                return render_template('area.html',titolo = 'AresPersonale')
            else:
                flash('Password non corrretta')
                return redirect (url_for('login'))
            


    return render_template('login.html',titolo = 'Accedi')
        
      
            
app.run(debug=True)
