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
#command = "CREATE TABLE bloginfo(username TEXT, blogid INTEGER, title TEXT, content TEXT);"
#c.execute(command) # run SQL statement

#==============================================================================

#USERINFO TABLE COMMANDS
#returns password for a given username, if username is nonexistant return None
def fetchPassword(username):
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
         if row[0] == username:
            return row[1]
         else:
            return None

#adds a user to the userinfo table
def addUser(username, password):
    command = "SELECT * FROM userinfo"
    c.execute(command)
    data = c.fetchall()

#______________________________________________________________________________

#BLOGINFO TABLE COMMANDS
#returns blog title given its blogid
def fetchBlogTitle(blogid):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[1] == blogid:
            return row[2]

#returns blog content given its blogid
def fetchBlogContent(blogid):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()
    for row in data:
        if row[1] == blogid:
            return row[3]

#returns all blog titles
def fetchAllBlogTitles():
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()

#returns all blog content
def fetchAllBlogContent():
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()

#adds a post to the blogs table
def addBlog(username, blogid, title, content):
    command = "INSERT INTO bloginfo VALUES('{}', {}, '{}', '{}')".format(username, blogid, title, content)
    c.execute(command)
    db.commit()


#deletes a blog from the blogs table
def deleteBlog(blogid):
    command = "SELECT * FROM bloginfo"
    c.execute(command)
    data = c.fetchall()

addBlog("bruh", 1, "tre", "ddf")
db.close()
