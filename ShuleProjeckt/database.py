
import sqlite3


def studentdata():
    connection = sqlite3.connect('students.db')
    connection.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,  Nummer TEXT, Firstname TEXT, \
         Lastname TEXT, Age TEXT, Phone TEXT, Email TEXT, Gender TEXT, Class TEXT);")
    connection.commit()
    connection.close()

   
studentdata()

