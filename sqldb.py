import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE= "glit.db"
db = sqlite3.connect("glit.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
#==============================================================================
#create table
command = "CREATE TABLE userinfo(username TEXT, password TEXT);"
c.execute(command) # run SQL statement

#create table
command = "CREATE TABLE blogs(username TEXT, blogid INTEGER, title TEXT, content TEXT);"
c.execute(command) # run SQL statement

#==============================================================================
#returns password given a username, if username is not present in the database return None
def fetchUsername(username):
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[0] = username:
            return row[1]
        else:
            return None

def fetchBlog(blogid):

def fetchAllBlogs():

def addUser(username, password):

def addPost(username, blogid, title, content):
