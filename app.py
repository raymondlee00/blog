from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import sqlite3   #enable control of an sqlite database

app = Flask(__name__)


@app.route('/')
def hello():
    print(__name__)
    return render_template("appuserdebug.html")


@app.route('/register')
def register():
	if len(request.args) == 0:
		return render_template("register.html")
	else:
		command = "INSERT INTO users VALUES('{}','{}');".format(request.args["usernamein"], request.args["passwordin"])
		runsqlcommand(command)
		return "you are now registered!!"


@app.route('/auth')
def auth():
	if len(request.args) == 0:
		# throw Exception e
		pass
	else:
		# check if uname is in sql
		command = "SELECT * FROM users where name = '{}'".format(request.args["username"])
		pair = runsqlcommand(command)
		if len(pair) == 0:
			# throw exception
			pass
		else:
			if (request.args["password"] == pair[1]):
				session["username"] = request.args[0]
				pass


def runsqlcommand(command):
	DB_FILE="data.db"
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

# z = runsqlcommand("INSERT INTO users VALUES('Richard','Mutt');")
# print(z)
