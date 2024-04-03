from tkinter import *
from tkinter import ttk
import sqlite3

class Quiz:
    def __init__(self, root, subject):
        self.root = root
        self.root.title("Quiz")
        self.current_question_index = 0
        self.subject = subject
        self.questions = self.load_questions_from_database()
        self.display_question()

    def load_questions_from_database(self):
        connection = sqlite3.connect('QuizBowl.db')
        cursor = connection.cursor()
        cursor.execute(f"SELECT question, option1, option2, option3, option4, correct_answer FROM {self.subject}")
        questions = cursor.fetchall()
        connection.close()
        return questions

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            question_text = question_data[0]
            options = question_data[1:5]
            correct_answer = question_data[5]
            self.question_answer = QuestionAnswer(self.root, question_text, options, correct_answer, self.next_question)
        else:
            self.show_result()

    def next_question(self):
        self.current_question_index += 1
        self.display_question()

    def show_result(self):
        result_window = Tk()
        result_label = Label(result_window, text="Quiz Finished!")
        result_label.pack()

class QuestionAnswer:
    def __init__(self, master, strQuestion, listAnswers, correctAnswer, callback):
        self.correctAnswer = correctAnswer
        self.callback = callback 
        self.frameQA = ttk.Frame(master, relief="raised", padding=(5, 5))
        self.frameQA.pack()
        self.label1 = ttk.Label(self.frameQA, text=strQuestion)
        self.label1.pack()
        self.answerOptions = ttk.Combobox(self.frameQA, values=listAnswers)
        self.answerOptions.pack()
        self.testButton = ttk.Button(self.frameQA, text="Submit", command=self.checkAnswer)
        self.testButton.pack()
        self.labelFeedback = ttk.Label(self.frameQA)
        self.labelFeedback.pack()

    def checkAnswer(self):
        if self.answerOptions.get() == self.correctAnswer:
            self.labelFeedback.config(text="Correct!", foreground="green")
        else:
            self.labelFeedback.config(text="Incorrect!", foreground="red")

        self.callback()

class SelectSubject:
    def __init__(self, root):
        self.root = root
        self.root.title("Pick a Subject")
        self.button_to_quiz = ttk.Button(self.root, text="Go to Quiz", command=self.open_quiz)
        self.button_to_quiz.pack(pady=10)
        
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
    
    def setup_ui(self):
        self.subjects = self.load_subjects()
        self.subject_combobox = ttk.Combobox(self.root, values=self.subjects)
        self.subject_combobox.pack(pady=10)
        self.button_to_quiz.pack(pady=10)

root = Tk()
app = SelectSubject(root)
app.setup_ui()
root.mainloop()
