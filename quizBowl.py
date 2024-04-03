from tkinter import *
from tkinter import ttk
import sqlite3

class Quiz:
    def __init__(self, root, subject):
        self.root = root
        self.root.title("Quiz")
        self.subject = subject
        self.questions = self.load_questions_from_database()
        self.display_questions()

    def load_questions_from_database(self):
        connection = sqlite3.connect('QuizBowl.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT question, option1, option2, option3, option4, correct_answer FROM {self.subject}")
        questions = cursor.fetchall()
        connection.close()
        return questions

    def display_questions(self):
        for question_data in self.questions:
            question_text = question_data[0]
            options = question_data[1:5]
            correct_answer = question_data[5]
            QuestionAnswer(self.root, question_text, options, correct_answer)

class QuestionAnswer:
    def __init__(self, master, strQuestion, listAnswers, correctAnswer):
        self.correctAnswer = correctAnswer
        self.frameQA = ttk.Frame(master, relief="raised", padding=(5, 5))
        self.frameQA.pack()
        self.label1 = ttk.Label(self.frameQA, text=strQuestion)
        self.label1.pack()
        self.answerOptions = ttk.Combobox(self.frameQA, values=listAnswers)
        self.answerOptions.pack()
        self.labelFeedback = ttk.Label(self.frameQA)
        self.labelFeedback.pack()
        self.testButton = ttk.Button(self.frameQA, text="Submit", command=self.checkAnswer)
        self.testButton.pack()

    def checkAnswer(self):
        if self.answerOptions.get() == self.correctAnswer:
            self.labelFeedback.config(text="Correct!", foreground="green")
        else:
            self.labelFeedback.config(text=f"Incorrect! The correct answer is: {self.correctAnswer}", foreground="red")

class SelectSubject:
    def __init__(self, root):
        self.root = root
        self.root.title("Pick a Subject")
        self.button_to_quiz = ttk.Button(self.root, text="Go to Quiz", command=self.open_quiz)
        
    def open_quiz(self):
        subject = self.subject_combobox.get()
        if subject:
            self.root.destroy()
            quiz_window = Tk()
            Quiz(quiz_window, subject)

    def load_subjects(self):
        connection = sqlite3.connect('QuizBowl.db')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        subjects = [row[0] for row in cursor.fetchall()]
        connection.close()
        return subjects
    
    def select_subject_window(self):
        self.subjects = self.load_subjects()
        self.subject_combobox = ttk.Combobox(self.root, values=self.subjects)
        self.subject_combobox.pack(pady=10)
        self.button_to_quiz.pack(pady=10)

root = Tk()
app = SelectSubject(root)
app.select_subject_window()
root.mainloop()
