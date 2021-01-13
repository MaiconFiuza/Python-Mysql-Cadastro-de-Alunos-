import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def Delete(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0, select['nome'])
    e3.insert(0, select['course'])
    e4.insert(0, select['fee'])

def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="root",database="record")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO user(id, nome, course,fee) VALUES (%s,%s,%s,%s)"
        val =(studid,studname,coursename,feee)
        mycursor.execute(sql,val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Informação","Aluno cadastrado com sucesso")
        e1.delete(0,END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except EXCEPTION as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="record")
    mycursor = mysqldb.cursor()

    try:
        sql = "UPDATE user set nome= %s, course= %s, fee=%s, where id=%s"
        val = (studname, coursename, feee,studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Informação", "Aluno atualizado com sucesso")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except EXCEPTION as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="record")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from record where id=%s"
        val = (studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Informação", "Aluno excluído com sucesso")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except EXCEPTION as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="root", database="record")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,nome,course,fee FROM user")
    records = mycursor.fetchall()
    print(records)

    for i,(id,nome,course,fee) in enumerate(records,start=1):
        listBox.insert("","end",value=(id,nome,course,fee))
        mysqldb.close()

root = Tk()

root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root,text="Registro de Aluno", fg="black", font=(None,30)).place(x=400,y=5)

tk.Label(root, text="Id do Aluno").place(x=10,y=10)
Label(root, text="Nome do Aluno").place(x=10,y=40)
Label(root, text="Curso").place(x=10,y=70)
Label(root, text="Fee").place(x=10,y=100)

e1 = Entry(root)
e1.place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)

e3 = Entry(root)
e3.place(x=140,y=70)

e4 =Entry(root)
e4.place(x=140,y=100)

Button(root, text="Add", command=Add, height=3,width=13).place(x=30,y=130)

Button(root, text="Update", command=update,height=3,width=13).place(x=140,y=130)
Button(root, text="Delete", command=delete,height=3,width=13).place(x=250,y=130)

cols=('id','nome','course','fee')
listBox=ttk.Treeview(root, columns=cols,show='headings')

for col in cols:
    listBox.heading(col,text=col)
    listBox.grid(row=1,column=0,columnspan=2)
    listBox.place(x=10,y=200)

show()
listBox.bind('<Double-Button-1>',Delete)
root.mainloop()