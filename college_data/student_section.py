from tkinter import *
from tkinter import ttk,font
import pymysql
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def display() :
         s_marks = Tk()
         s_marks.title("Student_section")
         s_marks.state("zoomed")
         v = font.Font(family="Poppins", size=16, weight="bold")
         s = font.Font(family="Poppins", size=10)
         style = ttk.Style()
         style.configure("TButton", font=("Poppins", 10))

         #--->variables<---
         roll = StringVar()
         name = StringVar()
         marks = StringVar()


         def back():
              s_marks.destroy()
              import interface


         def database() :
              db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="college_database")
              sql = "select Students.roll_no,avg((Class_test.ct_1+Class_test.ct_1)/2) as avg_marks,Students.name from Students inner join Class_test on Class_test.roll_no = Students.roll_no where Students.roll_no = %s;"
              value = g.get()
              cur = db.cursor()
              cur.execute(sql,value)
              f = cur.fetchall()
              if f[0][0]!= None :
                          g.delete(0,END)
                          t.delete(0,END)
                          g.insert(0,f[0][0])
                          t.insert(0,f[0][1])
                          if f[0][1]>7 :
                              p ="pass"
                          else :
                              p ="fail"
                          ttk.Label(s_marks, text=p, font=s).place(x=634, y=312, width=50, height=30)
              else:
                   g.delete(0,END)
                   t.delete(0,END)
                   engine.say("data not found")
                   engine.runAndWait()

         ttk.Label(s_marks, text="Jhada Sirha Government Engineering College", font=v).place(x=440, y=150, width=500,
                                                                                             height=40)
         ttk.Label(s_marks, text="Student's Result  ", font=v).place(x=570, y=194, width=250, height=40)

         ttk.Label(s_marks, text="Roll no.", font=s).place(x=550, y=244, width=70, height=30)
         ttk.Label(s_marks, text=":", font=s).place(x=622, y=244, width=10, height=30)
         g = ttk.Entry(s_marks,textvariable=roll, font=s)
         g.place(x=634, y=244, width=150, height=30)

         ttk.Label(s_marks, text="Marks", font=s).place(x=550, y=278, width=70, height=30)
         ttk.Label(s_marks, text=":", font=s).place(x=622, y=278, width=10, height=30)
         t = ttk.Entry(s_marks,textvariable=marks, font=s)
         t.place(x=634, y=278, width=150, height=30)

         ttk.Label(s_marks, text="Pass/Fail", font=s).place(x=550, y=312, width=70, height=30)
         ttk.Label(s_marks, text=":", font=s).place(x=622, y=312, width=10, height=30)


         ttk.Button(s_marks, text="save", command=database).place(x=585, y=385, width=150, height=30)
         ttk.Button(s_marks, text="back to home", command=back).place(x=585, y=425, width=150, height=30)


         s_marks.mainloop()


