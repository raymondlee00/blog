from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__)

@app.route('/')
def hello():
    print(__name__)
    return 'reeeee'

if __name__ == '__main__':
    app.debug = True
    app.run()
