import sqlite3
from tkinter.constants import N


def student_data():
    connection = sqlite3.connect('students.db')
    connection.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,  Student_Id TEXT, Firstname TEXT, \
         Lastname TEXT, Age TEXT, Phone TEXT, Email TEXT, Clas TEXT);")
    connection.commit()
    connection.close()


def add_data(Student_Id, Firstname, Lastname, Age, Phone, Email, Clas):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", \
         (Student_Id, Firstname, Lastname, Age, Phone, Email, Clas))
    connection.commit()
    connection.close()

def view_data():
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete_data(id):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    connection.commit()
    connection.close


def search_data(Student_Id="", Firstname="", Lastname="", Age="", Phone="", Email="", Clas=""):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE Student_Id=? OR Firstname=? OR Lastname=? OR Age=? OR Phone=? OR Email=? OR Clas=?", \
              (Student_Id, Firstname, Lastname, Age, Phone, Email, Clas))
    rows = cursor.fetchall()
    connection.close()
    return rows



def update_data(id, Student_Id="", Firstname="", Lastname="", Age="", Phone="", Email="", Clas=""):
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET Student_Id=?, Firstname=?, Lastname=?, Age=?, Phone=?, Email=?, Clas=?", \
              (Student_Id, Firstname, Lastname, Age, Phone, Email, Clas, id))
    connection.commit()
    connection.close()
   

student_data()

