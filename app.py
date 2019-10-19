from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import sqlite3   #enable control of an sqlite database

app = Flask(__name__)

DB_FILE="data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

@app.route('/')
def hello():
    print(__name__)
    return 'reeeee'

if __name__ == '__main__':
    app.debug = True
    app.run()
