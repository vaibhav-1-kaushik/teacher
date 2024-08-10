from tkinter import *
from tkinter import ttk,font
import Teacher_section
import pyttsx3
import pymysql

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def C_marks() :
         c_Marks = Tk()
         c_Marks.title("Class_test")
         c_Marks.state("zoomed")
         v = font.Font(family="Poppins", size=16, weight="bold")
         s = font.Font(family="Poppins", size=10)
         style = ttk.Style()
         style.configure("TButton", font=("Poppins", 10))

         #--->variables<---
         roll_no = StringVar()
         subject = StringVar()
         ct_1 = StringVar()
         ct_2 = StringVar()

         def entry():
             engine.say("enter values for given filed")
             engine.runAndWait()

         def check():
             text = ["Roll number", "subject", "CT 1 marks", "CT 2 marks"]
             var = [roll_no,subject,ct_1,ct_2]
             v = 0
             for f in var:
                 if f.get() == "":
                     engine.say(f"enter {text[v]}")
                     engine.runAndWait()
                     return 0
                 v = v + 1

         def back() :
              c_Marks.destroy()
              Teacher_section.t_Desk()

         def database() :
                d_v = check()
                if d_v !=0 :
                         db =pymysql.connect(host = "localhost",user="root",password="Vaibhav123@",database="college_database")
                         sql = "insert into Class_test values(%s,%s,%s,%s)"
                         sql2 = "select * from Students where roll_no = %s"
                         value =[roll_no.get(),subject.get(),ct_1.get(),ct_2.get()]

                         cur = db.cursor()
                         if cur.execute(sql2,value[0]) :
                                                      cur.execute(sql,value)
                                                      db.commit()
                                                      engine.say("saved successfully")
                                                      engine.runAndWait()
                                                      roll_no.set("")
                                                      subject.set("")
                                                      ct_1.set("")
                                                      ct_2.set("")
                         else :
                             engine.say("Student is not registered")
                             engine.runAndWait()



         ttk.Label(c_Marks, text="Jhada Sirha Government Engineering College", font=v).place(x=440, y=150, width=500,
                                                                                             height=40)
         ttk.Label(c_Marks, text="Student's Marks Entry ", font=v).place(x=570, y=194, width=250, height=40)

         ttk.Label(c_Marks, text="Roll no.", font=s).place(x=550, y=244, width=70, height=30)
         ttk.Label(c_Marks, text=":", font=s).place(x=622, y=244, width=10, height=30)
         ttk.Entry(c_Marks,textvariable=roll_no, font=s).place(x=634, y=244, width=150, height=30)

         ttk.Label(c_Marks, text="subject", font=s).place(x=550, y=278, width=70, height=30)
         ttk.Label(c_Marks, text=":", font=s).place(x=622, y=278, width=10, height=30)
         ttk.Entry(c_Marks,textvariable=subject, font=s).place(x=634, y=278, width=150, height=30)

         ttk.Label(c_Marks, text="Class_test-1", font=s).place(x=550, y=312, width=70, height=30)
         ttk.Label(c_Marks, text=":", font=s).place(x=622, y=312, width=10, height=30)
         ttk.Entry(c_Marks,textvariable=ct_1, font=s).place(x=634, y=312, width=150, height=30)

         ttk.Label(c_Marks, text="Class_test-2", font=s).place(x=550, y=346, width=70, height=30)
         ttk.Label(c_Marks, text=":", font=s).place(x=622, y=346, width=10, height=30)
         ttk.Entry(c_Marks, textvariable=ct_2,font=s).place(x=634, y=346, width=150, height=30)

         ttk.Button(c_Marks, text="save", command=database).place(x=585, y=385, width=150, height=30)
         ttk.Button(c_Marks, text="back to home", command=back).place(x=585, y=425, width=150, height=30)

         c_Marks.after(1000,entry)
         c_Marks.mainloop()

