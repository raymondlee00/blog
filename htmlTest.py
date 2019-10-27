from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import time
import sqlite3   #enable control of an sqlite database
import sqldb


app = Flask(__name__)
app.secret_key = 'hfjkafhrku'
@app.route('/')
def test():
	print(__name__)
	return render_template("viewBlog.html", username = "alex", posts = {"I am the title":"this is where post content will go.", "I am post2":"beep boop"})##For html testing purposes

##@app.route('/editPost')
##def editPost():
	print(__name__)
    ##title = request.args["postTitle"]
    ##title = title.substring(5)
##    return render_template("editPost.html", post = ["I was the title","this is where old post content will go."])

if __name__ == '__main__':
	app.debug = True
	app.run()
