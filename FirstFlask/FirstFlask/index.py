from os import environ

from flask import Flask,render_template, redirect, url_for, request, flash, session
from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask.migrate import Migrate

#from flask_wtf import Form
#from wtforms.fields import BooleanField, TextField, PasswordField, validators
#from passlib.hash import sha256_crypt
#-from MySQLdb import escape_string as thwart*/

import gc

app=Flask(__name__)
@app.route('/')
@app.route('/login', methods=['GET','POST'])
#@app.route('/register/', methods=['GET,''POST'])

#def register():
#    try:
#        form = RegistrationForm(request.form)

#        if request.method == "POST" and form.validate():
#            username = form.username.data
#            email = form.email.data
#            password = sha256_crypt.encrypt((str(form.password.data)))
#            c, conn = Connection()

#            x = c.execute("SELECT * FROM users WHERE username = (%s)",(thwart(username)))

#            if int(x) > 0:
#                flash("That username is already taken, use another")
#                return render_template('register.html', form=form)

#            else:
#                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
#                          (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))
                
#                conn.commit()
#                flash("Thanks for registering!")
#                c.close()
#                conn.close()
#                gc.collect()

#                session['logged_in'] = True
#                session['username'] = username

#                return redirect(url_for('dashboard'))

#        return render_template("register.html", form=form)

#   except Exception as e:
#        return(str(e))
#		        
#
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Username or Password. Try Again'
        else:
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

def index():
    data = {
        "title": "Home Page",
        "msg": "Hello World from Flask for Python!!!",
        "me" : environ.get("USERNAME")}
    return render_template("index.html",data=data)

if __name__ == "__main__" :
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)