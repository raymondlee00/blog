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
	if len(request.args) == 1:
		session.pop("username")
		pass
	else:
		# check if uname is in sql
		command = "SELECT * FROM userinfo where username = '{}'".format(request.args["username"])
		pair = runsqlcommand(command)
		if len(pair) == 1:
			return ("incorrect fool <a href = '/'></a>")
		else:
			if (request.args["password"] == pair[0][1]):
				print("#####################")
				print(len(request.args))
				print(type(request.args["username"]))
				print(type(pair[0][1]))
				print("#####################")
				session["username"] = request.args["username"]
				return ("you are logged in!! " + session["username"])
				pass


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
