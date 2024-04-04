# Quarterly-Assessment-3

This repository consists of multiple files to create two GUIs that will allow users to pick a subject and then present them with a multiple choice quiz of questions regarding selected subject. 

## quizBowl.py

This file is the main application file. Upon running, a window will pop up prompting the user to select a subject out of the five choices: Accounting, ManagerialFinance, ComputerForensics, ApplicationsDevelopment, and FederalTax. After selecting a subject, the user will click the "Go to quiz" button. Upon clicking the button, the first window will close and a new one will appear. 

The second window will provide the user with ten multiple choice questions pertaining to the stated subject. Each question has a submit button; however, the button is disable upon clicking once. Therefore, there is only one try per question. However, don't be scared, a label will provide you with the correct answer if you choose one of the incorrect options. 

If you would like to choose a different subject, please close the window and rerun the program. This will take you back to the Pick a Subject window. 

To create this file, the pack geometry manager, several classes, specifically defined functions, labels, buttons, frames, and comboboxes, were used. In addition, it was required to create a link to the database using SQLite. 

## QuizBowl.db

This file is the database, which stores five seperate tables with the subjects : Accounting, ManagerialFinance, ComputerForensics, ApplicationsDevelopment, and FederalTax. All of these tables have been populated with ten multiple choice questions. 

## Create Folder

This folder hosts four files used to populate the database at which the mutilple choice quiz will pull from. 

### createQuestions.py

This file was used to specifically add fifty questions to the database. Each addition specifics a question, four options, a correct answer, and the proper subject catergory they fall into. 

### createTable.py

This file was used to create the five tables that pretain to the listed subjects. Each table holds ten of the fifty questions mentioned above. 

### viewingQuestions.py

This file was used to view the questions entered in each table. I have programmed it to ask the specific table to pull the questions from. 

### viewingTableNames.py

This file was used to view all tables populated into the database. It presents them as a list in the terminal. 
