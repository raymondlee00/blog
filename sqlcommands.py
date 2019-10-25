import sqlite3   #enable control of an sqlite database

class SQLHandler(object):
    """docstring for SQLHandler."""

    def __init__(self, file):
        super(SQLHandler, self).__init__()
        self.db = sqlite3.connect(file) #open if file exists, otherwise create
        self.c = db.cursor()               #facilitate db ops

    def fetchPassword(self, username):
        command = "SELECT * FROM userinfo"
        c.execute(command)
        data = c.fetchall()
        for row in data:
             if row[0] == username:
                return row[1]
             else:
                return None
