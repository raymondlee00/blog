from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import sqlite3   #enable control of an sqlite database
import sqldb

app = Flask(__name__)
app.secret_key = 'hfjkafhrku'


@app.route('/')
def hello():
    print(__name__)
    return render_template("login.html")


@app.route('/debug')
def hddd():
    print(__name__)
    return session["username"]

@app.route('/register')
def register():
	if len(request.args) == 0:
		return render_template("register.html")
	else:
		command = "INSERT INTO userinfo VALUES('{}','{}');".format(request.args["usernamein"], request.args["passwordin"])
		runsqlcommand(command)
		return "you are now registered!! <br> <br> <a href = '/'> go to login </a>"


@app.route('/auth')
def auth():
	if len(request.args) == 0:
		session.pop("username")
		return("<a href = '/'> ur logged out <br>go home</a>")

	command = "SELECT * FROM userinfo where username = '{}'".format(request.args["username"])
	pair = runsqlcommand(command)
	if len(pair) == 0:
		return ("incorrect fool <a href = '/'></a>")
	else:
		if (request.args["password"] == pair[0][1]):
			session["username"] = request.args["username"]
			return redirect("/welcome")
		else:
			return("WRONG PASSWORD" + str(pair))

@app.route('/welcome')
def welcome():
	return render_template("welcome.html", username = session["username"])


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
