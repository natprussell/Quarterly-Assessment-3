from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Accounting Quiz")

class SelectSubject:
    def __init__(self, root):
        self.root = root
        self.root.title("Pick a Subject")
        self.button_to_quiz = ttk.Button(self.root, text="Go to Quiz", command=self.open_quiz)
        self.button_to_quiz.pack(pady=10)
    def open_quiz(self):
        self.root.destroy()
        quiz_window = ttk.Tk()
        Quiz(quiz_window)

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
    

class QuestionAnswer:
    def __init__ (self,master,strQuestion,listAnswers, correctAnswer):
        self.correctAnswer= correctAnswer
        self.frameQA= ttk.Frame (master, relief= "raised", padding=(5,5))
        self.frameQA.pack()
        self.label1= ttk.Label(self.frameQA, test= strQuestion)
        self.label1.pack()
        self.answerOptions=ttk.Combobox(self.frameQA)
        self.answerOptions.pack()
        self.answerOptions.comfig(values=listAnswers)
        self.testButton= ttk.Button(self.frameQA, text="Submit", command= self.checkAnswer)
        self.testButton.pack()
        self.labelFeedback= ttk.Label(self.frameQA)
        self.labelFeedback.pack()
    def checkAnswer (self):
        if self.answerOptions.get() == self.correctAnswer:
            self.labelFeedback.config (text= "Correct!", foreground= "green")
        else:
            self.labelFeedback.config (text= "Incorrect!", foreground= "red")



