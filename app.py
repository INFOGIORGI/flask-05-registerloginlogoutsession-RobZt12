from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")



app.run()
