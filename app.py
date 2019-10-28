from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import time
import sqlite3  # enable control of an sqlite database
import sqldb


app = Flask(__name__)
app.secret_key = 'hfjkafhrku'
@app.route('/test')
def test():
    print(__name__)
    return render_template("results.html")  # For html testing purposes


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

# REdirect to hmer
@app.route('/register')
def register():
    if len(request.args) == 0:
        return render_template("register.html")
    else:
        existencecommand = "SELECT * FROM userinfo WHERE username = '{}'".format(
            request.args["usernamein"])
        if(len(runsqlcommand(existencecommand)) == 0):
            command = "INSERT INTO userinfo VALUES('{}','{}');".format(
                request.args["usernamein"], request.args["passwordin"])
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

    command = "SELECT * FROM userinfo where username = '{}'".format(
        request.args["username"])
    pair = runsqlcommand(command)
    if len(pair) == 0:
        return render_template("login.html", error="Your username is unfortunately WRONG")
    else:
        if (request.args["password"] == pair[0][1]):
            session["username"] = request.args["username"]
            return redirect("/welcome")
        else:
            return render_template("login.html", error="Your password is unfortunately WRONG")


@app.route('/welcome')
def welcome():
    command = "SELECT * FROM bloginfo"
    data = runsqlcommand(command)
    allBlogs = []
    for row in data:
        if row[0] == session["username"] and not(row[3] in allBlogs):
            allBlogs.append(row[3])
    return render_template("welcome.html", blogNames=allBlogs, username=session["username"])


@app.route('/createPost')
def createPost():
    blogName = request.args["blogName"]
    return render_template("createPost.html", blogName=blogName)


@app.route('/addpost')
def postadd():
    blogName = request.args["blogName"]
    title = request.args["postTitle"]
    content = request.args["postContent"]
    command = "SELECT * FROM bloginfo"
    dict = runsqlcommand(command)
    for row in dict:
        if (row[1] == title):
            flash("Title already exists. Change Title")
            return redirect(url_for("createPost", blogName = blogName))

    command = "INSERT INTO bloginfo VALUES('{}','{}', '{}', '{}')".format(
        session["username"], title, content, blogName)
    runsqlcommand(command)
    flash("added post alright")
    return redirect(url_for("viewBlog", blogName=blogName))


@app.route("/delete")
def delete():
    entrytodelete = request.args["delete"]
    command = "SELECT * FROM bloginfo"
    data = runsqlcommand(command)
    blogname = ""
    for row in data:
        if entrytodelete == row[1]:
            blogname = row[3]
    command = "DELETE FROM bloginfo WHERE title = '{}'".format(entrytodelete)
    runsqlcommand(command)

    print(blogname)
    return redirect(url_for("viewBlog", blogName=blogname))


@app.route('/search')
def search():
    return render_template("search.html")


@app.route('/results')
def results():
    searchInput = request.args["searchInput"].lower()
    length = len(searchInput)
    command = "SELECT * FROM bloginfo where lower(title) LIKE '%{}%'".format(
        searchInput)
    allPosts = runsqlcommand(command)
    print(allPosts)
    # results = {}
    # for post in allPosts:
    #     title = post[0]
    #     content = post[1]
    #     titlecomp = title.lower()
    #     if (titlecomp.__contains__(searchInput)):
    #         results[title] = content

    return render_template("results.html", results=allPosts)


@app.route('/addBlog')
def addblog():
    #username = session["username"]
    blogname = request.args["blogName"]
    title = ""
    content = ""
    command = "SELECT * FROM bloginfo"
    dict = runsqlcommand(command)
    print(dict)
    for row in dict:
        if (row[3] == blogname):
            flash("Blog name already exists. Change it to add it")
            return redirect("/createBlog")
    command = "INSERT INTO bloginfo VALUES('{}','{}', '{}','{}')".format(
        session["username"], title, content, blogname)
    runsqlcommand(command)
    return redirect("/welcome")


@app.route('/createBlog')
def createBlog():
    return render_template("createBlog.html")


@app.route('/edit')
def edit():
    postTitle = request.args["edit"]
    command = "SELECT * FROM bloginfo"
    data = runsqlcommand(command)
    post = []
    for row in data:
        if postTitle == row[1]:
            post.append(row[1])
            post.append(row[2])
            blogName = row[3]
    return render_template("editPost.html", post=post, blogName=blogName)

@app.route('/editPost')
def editPost():
    newTitle = request.args["postTitle"]
    newContent = request.args["postContent"]
    oldTitle = request.args["oldTitle"]
    blogName = ""

    command = "SELECT * FROM bloginfo"
    data = runsqlcommand(command)
    for row in data:
        if oldTitle == row[1]:
            command = "UPDATE bloginfo SET title = '{}', content = '{}' WHERE title = '{}'".format(newTitle, newContent, oldTitle)
            blogName = row[3]
    runsqlcommand(command)
    return redirect(url_for("viewBlog", blogName = blogName))


@app.route('/showall')
def showall():
    command = "SELECT * FROM bloginfo"
    all = runsqlcommand(command)
    blogTitles = []
    for row in all:
        if not(row[3] in blogTitles):
            blogTitles.append(row[3])
    return render_template("showall.html", blogTitles=blogTitles)


@app.route('/viewBlog')
def viewBlog():
    # if not(blogName in locals()):
    blogName = request.args["blogName"]

    command = "SELECT * FROM bloginfo"
    data = runsqlcommand(command)
    dict = {}
    for row in data:
        if row[3] == blogName:
            user = row[0]
        if row[3] == blogName and not(row[1] == "" and row[2] == ""):
            dict.update({row[1]: row[2]})

    if user == session["username"]:
        return render_template("viewYourBlog.html", posts=dict, blogName=blogName, username=session["username"])
    else:
        return render_template("viewBlog.html", posts=dict, blogName=blogName, username=user)


def runsqlcommand(command):
    DB_FILE = "glit.db"
    db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
    c = db.cursor()  # facilitate db ops
    c.execute(command)
    if "select" in command.lower():
        return c.fetchall()
    db.commit()  # save changes
    db.close()  # close database


if __name__ == '__main__':
    app.debug = True
    app.run()
