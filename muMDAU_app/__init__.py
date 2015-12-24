from flask import Flask, request , session , redirect , url_for
from flask import render_template 
import sqlite3
app = Flask(__name__)

import subprocess
import setting 
import muMDAU_app.login 
import muMDAU_app.logout 
import muMDAU_app.panel
