from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name hospital and has the following columns - NAME,AGE,
    ADDRESS,TREATMENT,DOCTOR,FEE \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM PATIENT ;
    \nExample 2 - Tell me all the patitients treated by doctor Dr. Smith?, 
    the SQL command will be something like this SELECT * FROM PATIENT
    where DOCTOR="Dr. Smith"; 
    \n Example 3 - Tell me the name and treatemt treated by the doctor Dr. Smith?,
    the Sql command will be something like this SELECT NAME, TREATMENT FROM PATIENT WHERE DOCTOR = 'Dr. Smith';
    also the sql code should not have ``` in beginning or end and sql word in output
    
    """


]


st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("DATABASE INTERACTION USING LLM")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    #response=read_sql_query(response,"student.db")

    response=read_sql_query(response,"hospital.db")

    
    st.subheader("The Response is")
    for row in response:
        print(row)
        #response =  prompt(question)
        #print("----------------------------------------------------------------------")
        #print(f'SQL and response from user query {question}  \n  {response}')
        st.header(row)