# Brian, Vansh, Weichen
# SoftDev
# K19 -- Sessions Greetings
# 2022-11-3
# time spent: 30 mins

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           
from flask import redirect
from flask import url_for 

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    # return 'You are not logged in'
    return redirect(url_for('/login'))





@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
