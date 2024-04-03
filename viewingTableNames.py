import sqlite3
conn= sqlite3.connect('QuizBowl.db')
cr=conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
           
print(cr.fetchall())