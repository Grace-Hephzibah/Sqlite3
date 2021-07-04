# Importing the library
import sqlite3

# Connection to the database
connection = sqlite3.connect("Academy.db")
# Create the cursor
cursor = connection.cursor()

# Adding Records
student_data = [("Baskar", "C", "M", "75.2", "1998-05-17"),
               ("Sanjini", "A", "F", "95.6", "2002-11-01"),
               ("Varun", "B", "M", "80.6", "2001-03-14"),
               ("Priya", "A", "F", "98.6", "2002-01-01"),
               ("Tarun", "D", "M", "62.3", "1999-02-01")]

for p in student_data:
    format_str = """INSERT INTO Student (Rollno, Sname, Grade, gender, Average, birth_date)
    VALUES (NULL, "{name}", "{gr}", "{gender}", "{avg}", "{birthdate}");"""

    sql_command = format_str.format(name=p[0], gr=p[1], gender=p[2], avg=p[3], birthdate=p[4])

    cursor.execute(sql_command)

connection.commit()
connection.close()

print("Records added to student table")
