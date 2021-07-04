# Importing the library
import sqlite3

# Connection to the database
connection = sqlite3.connect("Academy.db")
# Create the cursor
cursor = connection.cursor()

# Execute the command to fetch all the data from the table student
cursor.execute("SELECT* FROM Student")

ans = cursor.fetchall()

#looping to print the data
for i in ans:
    print(i)