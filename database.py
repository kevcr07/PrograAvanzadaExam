import sqlite3
import datetime



    #Database#

con = sqlite3.connect("Project.DB")
c = con.cursor()

    #Tables#

c.execute("CREATE TABLE T_USERS ([USERID] INTEGER UNIQUE PRIMARY KEY,[USERNAME] TEXT, [PASSWORD] TEXT,  [EMAIL] TEXT, [AGE] INTEGER, [ROLE] TEXT, [DATE] DATE)")
print("Users table created")

c.execute("CREATE TABLE QUESTIONS([QUESTIONID] INTEGER PRIMARY KEY AUTOINCREMENT,[USER] INTEGER UNIQUE, [WORD] TEXT, FOREIGN KEY (USER) REFERENCES T_USERS(USERID))")
print("Questions table created")

c.execute("CREATE TABLE TEAMS([TEAMID] INTEGER PRIMARY KEY AUTOINCREMENT,[LEAD] INTEGER,[DESCRIPTION] TEXT,FOREIGN KEY (LEAD) REFERENCES T_USERS(USERID))")
print("Teams table created")

c.execute("CREATE TABLE MEMBERS([ID] INTEGER PRIMARY KEY AUTOINCREMENT,[TEAM] INTEGER,[USER] INTEGER,[DATE] DATE,FOREIGN KEY (USER) REFERENCES T_USERS(USERID),FOREIGN KEY (TEAM) REFERENCES TEAMS(TEAMID))")
print("Teams table created")

con.commit()
con.close()