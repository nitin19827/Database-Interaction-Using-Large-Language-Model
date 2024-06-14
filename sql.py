import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
DEPARTMENT VARCHAR(25),CGPA INT);

"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Nitin','Deep Learning','AIML',9.3)''')
cursor.execute('''Insert Into STUDENT values('Abhiash','Deep Learning','AIML',9.5)''')
cursor.execute('''Insert Into STUDENT values('Omkar','NLP','CSE(AIML)',8.6)''')
cursor.execute('''Insert Into STUDENT values('Tarun','FCN','CSE',8.2)''')
cursor.execute('''Insert Into STUDENT values('Mani Teja','NLP','CSE(AIDS)',8.8)''')
cursor.execute('''Insert Into STUDENT values('Mani Deepak','RPA','CSE(AIDS)',8.3)''')
cursor.execute('''Insert Into STUDENT values('Abhi Ram','FCN','CSE',9.6)''')
cursor.execute('''Insert Into STUDENT values('Krishna','NLP','CSE(AIML)',9.0)''')
cursor.execute('''Insert Into STUDENT values('Ajith','FCN','CSE(AIDS)',8.9)''')
cursor.execute('''Insert Into STUDENT values('Phani','Deep Learning','CSE',7.2)''')
cursor.execute('''Insert Into STUDENT values('Ram','NLP','AIML',9.6)''')
cursor.execute('''Insert Into STUDENT values('Rakesh','RPA','AIML',8.1)''')
cursor.execute('''Insert Into STUDENT values('Srikanth','Deep Learning','CSE(AIDS)',8.2)''')
cursor.execute('''Insert Into STUDENT values('Sai Kumar','Deep Learning','AIML',9.7)''')
cursor.execute('''Insert Into STUDENT values('Harsha','RPA','CSE',8.9)''')
cursor.execute('''Insert Into STUDENT values('Nani','RPA','CSE',7.2)''')
cursor.execute('''Insert Into STUDENT values('Ashok','RPA','CSE(AIDS)',8.4)''')


print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()