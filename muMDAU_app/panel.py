from muMDAU_app import app
from flask import request , session , render_template , url_for ,redirect
import sqlite3 
import setting
import os
@app.route('/admin' , methods=['GET','POST'])
def panel():
    if request.method == "POST":
            print("dd")
    else:
        if 'username' in session:
            return render_template('panel.html', username = session['username'])
        else:
            return redirect(url_for('loginp'))

