import sqlite3

# Establish connection to the database
connection = sqlite3.connect("hospital1.db")
cursor = connection.cursor()

# Define the table structure for the hospital database
table_info = """
CREATE TABLE PATIENT (
    NAME VARCHAR(50),
    AGE INT,
    ADDRESS VARCHAR(100),
    TREATMENT VARCHAR(50),
    DOCTOR VARCHAR(50),
    FEE REAL
);
"""

# Execute the table creation query
cursor.execute(table_info)

# Insert sample data into the database
cursor.execute('''INSERT INTO PATIENT VALUES('John Doe', 35, '123 Main St, City', 'Appendectomy', 'Dr. Smith', 1500.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Jane Smith', 45, '456 Elm St, Town', 'Fracture', 'Dr. Johnson', 2000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Bob Johnson', 28, '789 Oak St, Village', 'Flu', 'Dr. Anderson', 500.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Alice Williams', 60, '987 Pine St, Countryside', 'Heart Surgery', 'Dr. Brown', 10000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Sarah Parker', 50, '654 Maple St, Suburb', 'Pneumonia', 'Dr. White', 2500.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Michael Davis', 42, '321 Birch St, Rural', 'Dental Checkup', 'Dr. Green', 200.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Emily Taylor', 38, '234 Cedar St, Coastal', 'Eye Exam', 'Dr. Black', 150.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Daniel Wilson', 55, '876 Willow St, Mountains', 'Physical Therapy', 'Dr. Grey', 3000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Sophia Johnson', 25, '789 Elm St, Town', 'Influenza', 'Dr. Brown', 800.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Ethan Martinez', 32, '456 Oak St, Village', 'Broken Arm', 'Dr. Johnson', 1800.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Olivia Smith', 28, '123 Pine St, Countryside', 'Allergy Test', 'Dr. White', 600.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Mason Garcia', 45, '987 Birch St, Suburb', 'Knee Surgery', 'Dr. Black', 5000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Amelia Wilson', 60, '654 Maple St, Rural', 'Heart Checkup', 'Dr. Green', 1200.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Liam Taylor', 35, '876 Cedar St, Coastal', 'CT Scan', 'Dr. Grey', 700.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Ava Brown', 40, '321 Willow St, Mountains', 'MRI', 'Dr. Anderson', 1500.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Noah Lee', 50, '234 Oak St, Town', 'Physical Therapy', 'Dr. Smith', 3000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Isabella Clark', 48, '789 Elm St, Village', 'Eye Surgery', 'Dr. White', 4500.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('William Hernandez', 55, '123 Pine St, Countryside', 'Dental Cleaning', 'Dr. Brown', 100.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Sofia Martinez', 30, '987 Birch St, Suburb', 'Flu Shot', 'Dr. Johnson', 50.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('James Davis', 62, '876 Cedar St, Coastal', 'Colonoscopy', 'Dr. Black', 2000.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Charlotte Thompson', 38, '654 Maple St, Rural', 'Physical Exam', 'Dr. Green', 300.0)''')
cursor.execute('''INSERT INTO PATIENT VALUES('Benjamin Adams', 48, '321 Willow St, Mountains', 'Chiropractic', 'Dr. Grey', 500.0)''')


# Retrieve and print the inserted records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM PATIENT''')
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
