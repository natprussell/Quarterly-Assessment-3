import sqlite3

questions = [
    {
        'question': "Calculate the total assets given liabilities of $50,000 and equity of $30,000.",
        'options': ["$60,000","$70,000" , "$80,000", "$85,000"],
        'correct_answer': "$80,000",
        'subject': "Accounting"
    },
     {
        'question': "If a company has revenues of $100,000 and expenses of $60,000, what is the net income?",
        'options': ["$40,000","$50,000" , "$20,000", "$30,000"],
        'correct_answer': "$40,000",
        'subject': "Accounting"
    },
     {
        'question': "Determine the depreciation expense if the asset cost is $10,000 and has a useful life of 5 years.",
        'options': ["$2,000","$1,500" , "$2,025", "$2,300"],
        'correct_answer': "$2,000",
        'subject': "Accounting"
    },
    {
        "question": "What is the ending balance of an account with an initial balance of $5,000, additional investments of $2,000, and withdrawals of $1,000?",
        "options": ["$4,000","$7,000","$6,000","$3,000"],
        "correct_answer": "$6,000",
        "subject": "Accounting"
    },
    {
        "question": "If a company has current assets of $20,000 and current liabilities of $15,000, calculate the working capital.",
        "options": ["$7,500","$5,000","$25,000","$10,000"],
        "correct_answer": "$5,000",
        "subject": "Accounting"
    },
    {
        "question": "Calculate the book value of an asset with a cost of $8,000 and accumulated depreciation of $3,000.",
        "options": ["$7,000","$10,000","$11,000","$5,000"],
        "correct_answer": "$5,000",
        "subject": "Accounting"
    },
    {
        "question": "Find the gross profit margin if a company has sales of $80,000 and cost of goods sold of $40,000.",
        "options": ["0.6","1.5","0.4","0.5"],
        "correct_answer": "0.5",
        "subject": "Accounting"
    },
    {
        "question": "If a company issues 1,000 shares of common stock at $10 per share, calculate the total common stock value.",
        "options": ["$2,000","$20,000","$30,000","$10,000"],
        "correct_answer": "$10,000",
        "subject": "Accounting"
    },
    {
        "question": "Compute the return on equity (ROE) if net income is $15,000 and equity is $75,000.",
        "options": ["0.1","0.5","0.3","0.2"],
        "correct_answer": "0.2",
        "subject": "Accounting"
    },
    {
        "question": "What is the acid-test ratio if a company has current assets of $30,000, inventory of $10,000, and current liabilities of $15,000?",
        "options": ["0.67","0.33","0.5","1.33"],
        "correct_answer": "1.33",
        "subject": "Accounting"
    },
     {
        "question": "Unincorporated businesses are owned by:",
        "options": ["Sole proprietors", "Partnerships", "Both of the Above", "None of the Above"],
        "correct_answer": "Both of the Above",
        "subject": "ManagerialFinance"
    },
    {
        "question": "What is the primary goal for managers of publicly owned companies?",
        "options": ["Increase market share", "Minimize costs", "Maximize shareholder value", "Diversify portfolios"],
        "correct_answer": "Maximize shareholder value",
        "subject": "ManagerialFinance"
    },
    {
        "question": "What is intrinsic value?",
        "options": ["The current market price of a stock.", "The value of a stock as determined by its earnings.", "The estimate of a stock's 'true' value.", "A calculation based on future earnings potential."],
        "correct_answer": "The estimate of a stock's 'true' value.",
        "subject": "ManagerialFinance"
    },
    {
        "question": "Which financial statement shows a firm's revenues, expenses, and profits during a specific period of time?",
        "options": ["Balance Sheet", "Cash Flow Statement", "Income Statement", "Statement of Retained Earnings"],
        "correct_answer": "Income Statement",
        "subject": "ManagerialFinance"
    },
    {
        "question": "Which of the following is considered a fixed asset on the firm's balance sheet?",
        "options": ["Inventory", "Bonds", "Copyrights", "Notes payable"],
        "correct_answer": "D and F",
        "subject": "ManagerialFinance"
    },
    {
        "question": "Income not distributed to shareholders is: ",
        "options": ["Dividends", "Net Income", "Retained Earnings", "Earnings Per Share"],
        "correct_answer": "Retained Earnings",
        "subject": "ManagerialFinance"
    },
    {
        "question": "Which type of ratios capture a firm's ability to manage its debt?",
        "options": ["Profitability ratios", "Liquidity ratios", "Debt ratios", "Activity ratios"],
        "correct_answer": "Debt ratios",
        "subject": "ManagerialFinance"
    },
    {
        "question": "When the quick ratio increases, it generally indicates a(n) ______ in the firm's position?",
        "options": ["Deterioration", "No change", "Improvement", "Insolvency"],
        "correct_answer": "Improvement",
        "subject": "ManagerialFinance"
    },
    {
        "question": "Interest earned on principal and on prior period's interest: ",
        "options": ["Simple interest", "Nominal interest", "Compound interest", "None of the above"],
        "correct_answer": "Compound interest",
        "subject": "ManagerialFinance"
    },
    {
        "question": "A stream of equal periodic cash flows over a stated period of time: ",
        "options": ["Perpetuity", "Present Value", "Annuity", "Future Value"],
        "correct_answer": "Annuity",
        "subject": "ManagerialFinance"
    },
     {
        "question": "What is evidence that helps prove guilt?",
        "options": ["Exculpatory evidence", "Artifact", "Metadata", "Inculpatory evidence"],
        "correct_answer": "Inculpatory evidence",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is evidence that helps prove innocence?",
        "options": ["Artifact", "Metadata", "Exculpatory evidence", "Hash value"],
        "correct_answer": "Exculpatory evidence",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is any particular chunk of data?",
        "options": ["Metadata", "Exculpatory evidence", "Artifact", "Hash value"],
        "correct_answer": "Artifact",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is data about data?",
        "options": ["Hash value", "Artifact", "Exculpatory evidence", "Metadata"],
        "correct_answer": "Metadata",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is a number without intrinsic meaning and is also a 'digital fingerprint' for a hard drive?",
        "options": ["Inculpatory evidence", "Metadata", "Hash value", "Artifact"],
        "correct_answer": "Hash value",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is it called when a crime has probably been committed or is about to be committed?",
        "options": ["Reasonable suspicion", "Affidavit", "Warrant", "Probable cause"],
        "correct_answer": "Probable cause",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is it called when a crime has maybe been committed?",
        "options": ["Affidavit", "Warrant", "Reasonable suspicion", "Probable cause"],
        "correct_answer": "Reasonable suspicion",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is necessary to receive a warrant?",
        "options": ["Probable cause", "Reasonable suspicion", "Affidavit", "Warrant"],
        "correct_answer": "Affidavit",
        "subject": "ComputerForensics"
    },
    {
        "question": "This gives the right for search and seizure: ",
        "options": ["Probable cause", "Warrant", "Affidavit", "Reasonable suspicion"],
        "correct_answer": "Warrant",
        "subject": "ComputerForensics"
    },
    {
        "question": "What is any space that is not being used called?",
        "options": ["Unallocated space", "Hash value", "Artifact", "Metadata"],
        "correct_answer": "Unallocated space",
        "subject": "ComputerForensics"
    },
   {
        "question": "'Hello World' is an example of what?",
        "options": ["Integer", "Boolean", "String", "Float"],
        "correct_answer": "String",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "Python recognizes PEMDAS (true/false)?",
        "options": ["true", "false", "maybe", "sometimes"],
        "correct_answer": "true",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "Variable names can include spaces (true/false)?",
        "options": ["true", "false", "maybe", "sometimes"],
        "correct_answer": "false",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "Functions are stored in what?",
        "options": ["Scripts", "Packages", "Modules", "Libraries"],
        "correct_answer": "Modules",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "What kind of data types are either True or False?",
        "options": ["Numeric", "String", "Boolean", "List"],
        "correct_answer": "Boolean",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "An ordered collection of information is what?",
        "options": ["List", "Tuple", "Set", "Dictionary"],
        "correct_answer": "List",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "What module would you import to generate random integers?",
        "options": ["math module", "statistics module", "random module", "time module"],
        "correct_answer": "random module",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "An example of a loop that repeats an action a predefined number of times?",
        "options": ["while loop", "do-while loop", "for loop", "until loop"],
        "correct_answer": "for loop",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "An example of a loop that repeats an action until the program determines it needs to stop?",
        "options": ["for loop", "until loop", "do-while loop", "while loop"],
        "correct_answer": "while loop",
        "subject": "ApplicationsDevelopment"
    },
    {
        "question": "An ordered arrangement of objects/ elements is what?",
        "options": ["Sequence", "Array", "List", "Tuple"],
        "correct_answer": "Sequence",
        "subject": "ApplicationsDevelopment"
    },
     {
        "question": "What is a payment to support the cost of government?",
        "options": ["Fee", "Tariff", "Fine", "Tax"],
        "correct_answer": "Tax",
        "subject": "FederalTax"
    },
    {
        "question": "What is a person or organization that pays tax (includes individuals and corporations)?",
        "options": ["Taxpayer", "Beneficiary", "Recipient", "Donor"],
        "correct_answer": "Taxpayer",
        "subject": "FederalTax"
    },
    {
        "question": "What is right of a government to tax a particular taxpayer?",
        "options": ["Tax jurisdiction", "Tax exemption", "Tax evasion", "Tax break"],
        "correct_answer": "Jurisdiction",
        "subject": "FederalTax"
    },
    {
        "question": "What is the total amount of tax collected by the government and available for use?",
        "options": ["Tax expenditure", "Tax deficit", "Tax surplus", "Tax revenue"],
        "correct_answer": "Tax revenue",
        "subject": "FederalTax"
    },
    {
        "question": "What is tax levied on 'real' property?",
        "options": ["Income tax", "Excise tax", "Sales tax", "Real property tax"],
        "correct_answer": "Real property tax",
        "subject": "FederalTax"
    },
    {
        "question": "What is tax imposed on the retail sale of specific goods or services?",
        "options": ["Value-added tax", "Property tax", "Income tax", "Excise tax"],
        "correct_answer": "Excise tax",
        "subject": "FederalTax"
    },
    {
        "question": "What is tax imposed on individuals who live in a state and those who do not live in the state but earn income in the state?",
        "options": ["Corporate income tax", "Capital gains tax", "Personal income tax", "Sales tax"],
        "correct_answer": "Personal income tax",
        "subject": "FederalTax"
    },
    {
        "question": "These taxes provide help to workers who become unemployed through no fault of their own: ",
        "options": ["Social Security taxes", "Income taxes", "Property taxes", "Unemployment taxes"],
        "correct_answer": "Unemployment taxes",
        "subject": "FederalTax"
    },
    {
        "question": "A good tax must be which of the following: ",
        "options": ["Sufficient", "Convenient", "Fair", "All of the above"],
        "correct_answer": "All of the above",
        "subject": "FederalTax"
    },
    {
        "question": "What kind of revenue forecast assumes the tax base stays the same?",
        "options": ["Dynamic forecast", "Progressive forecast", "Static forecast", "Incremental forecast"],
        "correct_answer": "Static forecast",
        "subject": "FederalTax"
    }
   
]

connection = sqlite3.connect('QuizBowl.db')
cursor = connection.cursor()

subjects = set(question['subject'] for question in questions)
for subject in subjects:
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {subject} (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    correct_answer TEXT
                )''')

for question in questions:
    subject = question['subject']
    options = question['options']
    correct_answer = question['correct_answer']
    cursor.execute(f'''INSERT INTO {subject} (question, option1, option2, option3, option4, correct_answer)
                  VALUES (?, ?, ?, ?, ?, ?)''',
              (question['question'], options[0], options[1], options[2], options[3], correct_answer))


connection.commit()
connection.close()

print("Data inserted successfully.")