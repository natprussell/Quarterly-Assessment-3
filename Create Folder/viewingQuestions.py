import sqlite3
conn = sqlite3.connect('QuizBowl.db')
cr = conn.cursor()

table_name = input("What table would you like to view the questions and answers from?\n")

table_search = "SELECT * FROM " + table_name

cr.execute(table_search)
print(cr.fetchall())