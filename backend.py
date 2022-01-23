import sqlite3

def connect():
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY , name text , regno integer , mailid text , cgpa integer)")
    conn.commit()
    conn.close()

def insert(name,regno,mailid,cgpa):
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?) ",(name,regno,mailid,cgpa))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student ")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",regno="",mailid="",cgpa=""):
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR regno=? OR mailid=? OR cgpa=?",(name,regno,mailid,cgpa))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,regno,mailid,cgpa):
    conn=sqlite3.connect("students.db")
    cur=conn.cursor()
    cur.execute("UPDATE student SET name=?, regno=?, mailid=?,cgpa=? WHERE id=?",(name,regno,mailid,cgpa,id))
    conn.commit()
    conn.close()




connect()
#insert("Ajay",'19EEE22',"ajayronaldo@gmail.com",9.5)
#delete(4)
#update(6,"Tharshana","19EEE16","sanatrash@gmail.com",9.4)
#print(view())
#print(search(name="Hariprasath"))
