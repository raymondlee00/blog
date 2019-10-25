from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import time
import sqlite3   #enable control of an sqlite database

app = Flask(__name__)
app.secret_key = 'hfjkafhrku'
@app.route('/test')
def test():
	print(__name__)
	return render_template("results.html")##For html testing purposes


@app.route('/')
def hello():
	print(__name__)
	if "username" in session:
		return redirect("/welcome")
	return render_template("login.html")


@app.route('/debug')
def hddd():
	print(__name__)
	return session["username"]

#REdirect to hmer
@app.route('/register')
def register():
	if len(request.args) == 0:
		return render_template("register.html")
	else:
		existencecommand = "SELECT * FROM userinfo WHERE username = '{}'".format(request.args["usernamein"])
		if(len(runsqlcommand(existencecommand)) == 0):
			command = "INSERT INTO userinfo VALUES('{}','{}');".format(request.args["usernamein"], request.args["passwordin"])
			runsqlcommand(command)
			session["usernamein"] = request.args["passwordin"]
			return redirect("/")
		else:
			flash("username already exists")
			return redirect("/register")


@app.route('/auth')
def auth():
	if len(request.args) == 0:
		session.pop("username")
		return redirect("/")

	command = "SELECT * FROM userinfo where username = '{}'".format(request.args["username"])
	pair = runsqlcommand(command)
	if len(pair) == 0:
		return render_template("login.html", error = "Your username is unfortunately WRONG")
	else:
		if (request.args["password"] == pair[0][1]):
			session["username"] = request.args["username"]
			return redirect("/welcome")
		else:
			return render_template("login.html", error = "Your password is unfortunately WRONG")

@app.route('/welcome')
def welcome():
	return render_template("welcome.html", username = session["username"])


@app.route('/addpost')
def postadd():
	title = request.args["postTitle"]
	content = request.args["postContent"]
	command = "INSERT INTO bloginfo VALUES('{}', {}, '{}', '{}')".format(session["username"], time.time(), title, content)
	runsqlcommand(command)
	flash("added post alright")
	return redirect("/welcome")

@app.route('/search')
def search():
	return render_template("search.html")

@app.route('/results')
def results():
	return render_template("results.html")

@app.route('/createPost')
def createPost():
	return render_template("createPost.html")

@app.route('/showall')
def showall():
	return render_template("showall.html")

def runsqlcommand(command):
	DB_FILE="glit.db"
	db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops
	c.execute(command)
	if "select" in command.lower():
		return c.fetchall()
	db.commit() #save changes
	db.close()  #close database


if __name__ == '__main__':
	app.debug = True
	app.run()
