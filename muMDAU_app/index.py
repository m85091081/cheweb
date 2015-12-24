from muMDAU_app import app , setting
from flask import request , render_template , Blueprint
import subprocess , os
from subprocess import PIPE

main = Blueprint('main',__name__)

@main.route('/')
def index():
        return render_template('index.html')
