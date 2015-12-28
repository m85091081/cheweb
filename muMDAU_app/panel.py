from muMDAU_app import app
from database import countUSER , ManageSQL 
from flask import request , session , render_template , url_for ,redirect
@app.route('/admin' , methods=['GET','POST'])
def panel():
    if request.method == "POST":
            print("dd")
    else:
        if 'username' in session:
            return render_template('panel.html', username = session['username'])
        else:
            answer = countUSER.countAdmin()
            print(answer)
            if answer[0] == 0 :
                return redirect(url_for('init'))
            else:
                return redirect(url_for('loginp'))

@app.route('/init', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        user = request.form['buser']
        passd = request.form['bpass']
        import hashlib
        hashsha = hashlib.sha256(passd.replace('\n','').encode())
        ManageSQL.addUser(user,hashsha.hexdigest(),"1","0")
        return redirect(url_for('loginp'))
    else:
        return render_template('first.html')
    


