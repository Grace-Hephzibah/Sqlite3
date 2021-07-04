# Importing the library
import sqlite3

# Connection to the database
connection = sqlite3.connect("Academy.db")
# Create the cursor
cursor = connection.cursor()

# Creating a table
sql_command = """
CREATE TABLE Student(
Rollno INTEGER PRIMARY KEY,
Sname VARCHAR(20),
Grade CHAR(1),
gender CHAR(1),
Average DECIMAL(5,2),
birth_date DATE);
"""
cursor.execute(sql_command)

# Adding Records
sql_command = """INSERT INTO Student (Rollno, Sname, Grade, gender, Average, birth_date)
VALUES(NULL, "Akshay", "B", "M", "87.8", "2001-12-12");"""
cursor.execute(sql_command)

sql_command = """INSERT INTO Student (Rollno, Sname, Grade, gender, Average, birth_date)
VALUES(NULL, "Aravind", "A", "M", "92.50", "2000-08-17");"""
cursor.execute(sql_command)

connection.commit()
connection.close()

# Checking if the Database Creation and insertion is successful
print("Student Table Created")