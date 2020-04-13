import sqlite3

def selectlogin(user,passw):
    con = sqlite3.connect("Project.DB")
    c = con.cursor()
    query = ("SELECT USERID, PASSWORD, ROLE FROM T_USERS Where USERID =? AND PASSWORD = ?")
    c.execute(query,(user,passw))
    data = c.fetchall()
    return data

def selectusername(user):
    con = sqlite3.connect("Project.DB")
    c = con.cursor()
    query = ("SELECT USERNAME FROM T_USERS Where USERID =?")
    c.execute(query,[(user)])
    user = c.fetchall()
    return user

def insertuser(values):
    con = sqlite3.connect("Project.DB")
    c = con.cursor()
    c.executemany('INSERT INTO T_USERS (USERNAME, PASSWORD,EMAIL, AGE, ROLE) VALUES (?, ?, ?, ?,?)',values)
    con.commit()

def notify(mail):
    con = sqlite3.connect("Project.DB")
    c = con.cursor()
    query = ("SELECT USERID FROM T_USERS Where EMAIL =?")
    c.execute(query,[(mail)])
    user = c.fetchall()
    return user

def insertquestion(values):
    con = sqlite3.connect("Project.DB")
    c = con.cursor()
    c.executemany("INSERT INTO QUESTIONS (USER,WORD) VALUES (?,?)",values)
    con.commit() 

def selectusers():
    con = sqlite3.connect("Project.DB")
    c = con.cursor()

    query = ("SELECT USERID,USERNAME,PASSWORD,EMAIL,AGE,ROLE,WORD  FROM T_USERS INNER JOIN QUESTIONS ON USERID = USER")
    c.execute(query)
    data = c.fetchall()
    return data