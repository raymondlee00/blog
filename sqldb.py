import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE= "glit.db"
db = sqlite3.connect("glit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==============================================================================
#create table to store user information
#row[0] = username
#row[1] = password
#command = "CREATE TABLE userinfo(username TEXT, password TEXT);"
#c.execute(command) # run SQL statement

#create table to store blog information
#row[0] = username of blog creator
#row[1] = blogid
#row[2] = blog title
#row[3] = blog content
#command = "CREATE TABLE bloginfo(username TEXT, title TEXT, content TEXT);"
#c.execute(command) # run SQL statement

#______________________________________________________________________________
#USERINFO TABLE COMMANDS

#returns username as string given corresponding password
#if password is not present in userinfo database returns None
def fetchUsername(password):
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
         if row[1] == password:
            return row[0]
         else:
            return None

#returns password given corresponding username
#if username is not present in userinfo returns None
def fetchPassword(user):
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
         if row[0] == user:
            return row[1]
         else:
            return None

#adds a user to the userinfo table
def addUser(user, password):
    command = "INSERT INTO userinfo VALUES('{}', '{}')".format(user, password)
    c.execute(command)
    db.commit()

def printUserT():
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()
    print(data)

def deleteUser(user):
    command = "DELETE FROM userinfo WHERE username = '{}' ;".format(user)
    c.execute(command)
    data = c.fetchall()


#______________________________________________________________________________
#BLOGINFO TABLE COMMANDS

#returns blog title given corresponding username
def fetchBlogTitle(user):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[0] == user:
            return row[1]

#returns blog content given corresponding username
def fetchBlogContent(user):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[0] == user:
            return row[3]

#returns blog title and content as a dictionary
#title is the dict key and content is corresponding dict value
def fetchBlog(user):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    dict = {}
    for row in data:
        if row[0] == user:
            dict.update( {row[1] : row[2]} )
    return dict

#returns all blog titles as a list
def fetchAllBlogTitles():
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()

#returns all blog content as a list
def fetchAllBlogContent():
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()

#adds a post to bloginfo table
def addBlog(user, title, content):
    command = "INSERT INTO bloginfo VALUES('{}', '{}', '{}')".format(user, title, content)
    c.execute(command)
    db.commit()

#deletes a blog from the blogs table
def deleteBlog(user):
    command = "DELETE FROM userinfo WHERE username = '{}' ;".format(user)
    c.execute(command)
    data = c.fetchall()

def printBlogT():
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    print(data)

db.commit()
db.close()
