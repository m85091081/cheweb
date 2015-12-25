from muMDAU_app import app , setting
from flask import request , render_template, Markup , Blueprint
import subprocess , os ,markdown
from subprocess import PIPE

main = Blueprint('main',__name__)

@main.route('/')
def index():
        return render_template('index.html')

@app.route('/about')
def about():
    with open("./markdown/about.md","r") as f:
        content =  list(f)
        content = ''.join(content)
    content = Markup(markdown.markdown(content))
    return render_template('views.html',**locals())

@app.route('/teach')
def teach():
    return render_template('table.html')
