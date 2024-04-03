import sqlite3

conn = sqlite3.connect('QuizBowl.db')
cr = conn.cursor()

cr.execute('''
           CREATE TABLE IF NOT EXISTS Accounting (
           id INTEGER PRIMARY KEY,
           question TEXT,
           option1 TEXT,
           option2 TEXT,
           option3 TEXT,
           option4 TEXT,
           correct_answer TEXT)
           ''')

cr.execute('''
           CREATE TABLE IF NOT EXISTS ManagerialFinance (
           id INTEGER PRIMARY KEY,
           question TEXT,
           option1 TEXT,
           option2 TEXT,
           option3 TEXT,
           option4 TEXT,
           correct_answer TEXT)
           ''')

cr.execute('''
           CREATE TABLE IF NOT EXISTS ApplicationsDevelopment (
           id INTEGER PRIMARY KEY,
           question TEXT,
           option1 TEXT,
           option2 TEXT,
           option3 TEXT,
           option4 TEXT,
           correct_answer TEXT)
           ''')

cr.execute('''
           CREATE TABLE IF NOT EXISTS FederalTax (
           id INTEGER PRIMARY KEY,
           question TEXT,
           option1 TEXT,
           option2 TEXT,
           option3 TEXT,
           option4 TEXT,
           correct_answer TEXT)
           ''')

cr.execute('''
           CREATE TABLE IF NOT EXISTS ComputerForensics (
           id INTEGER PRIMARY KEY,
           question TEXT,
           option1 TEXT,
           option2 TEXT,
           option3 TEXT,
           option4 TEXT,
           correct_answer TEXT)
           ''')
conn.commit()
conn.close()
