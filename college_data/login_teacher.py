from tkinter import *
from tkinter import ttk ,font
import pymysql
import pyttsx3
import Teacher_section
import registration_teacher

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def log() :
           login = Tk()
           login.title("login_teachers")
           login.state("zoomed")
           v = font.Font(family="Poppins", size=16, weight="bold")
           s = font.Font(family="Poppins", size=10)
           style = ttk.Style()
           style.configure("TButton", font=("Poppins"))
           #--->variables<---

           t1 = StringVar()
           t2 = StringVar()

           #--->methods<----

           def voiceG():
               engine.say("welcome teacher")
               engine.runAndWait()
               engine.say("enter value in the field")
               engine.runAndWait()

           def check():
               text = ["user id", "password"]
               var = [t1,t2]
               v = 0
               for f in var:
                   if f.get() == "":
                       engine.say(f"enter {text[v]}")
                       engine.runAndWait()
                       return 0

                   v = v + 1
           def call_login():
                    v = check()
                    if v != 0 :
                          db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="college_database")
                          sql = "select u_id,name form from Teacher where u_id = %s and pw = %s"
                          value = [t1.get(),t2.get()]

                          cur = db.cursor()
                          if cur.execute(sql,value) :
                                             print(cur.fetchall())
                                             engine.say("login sucessfully")
                                             engine.runAndWait()
                                             t1.set("")
                                             t2.set("")
                                             login.destroy()
                                             Teacher_section.t_Desk()
                          else :
                              dis_registration()


           def call_registration() :

                    login.destroy()
                    registration_teacher.register()

           def  dis_registration() :
                        engine.say("Don't have any account firstly register yourself")
                        engine.runAndWait()
                        ttk.Label(login, text="Don't have any account,firstly register yourself", font=s).place(x=550,y=350, width=300,  height=30)
                        ttk.Button(login, text="Register", command=call_registration).place(x=550, y=385, width=250, height=30)

           ttk.Label(login,text="Welcome Teachers",font=v).place(x=570, y=150, width=250,height=40)
           ttk.Label(login,text="User_Id",font=s).place(x=550,y=200,width=70,height=30)
           ttk.Label(login, text=":", font=s).place(x=622, y=200, width=10, height=30)
           ttk.Entry(login,textvariable=t1,font=s).place(x=634, y=200, width=150, height=30)

           ttk.Label(login, text="Password",font=s).place(x=550, y=240, width=70, height=30)
           ttk.Label(login, text=":", font=s).place(x=622, y=240, width=10, height=30)
           ttk.Entry(login,textvariable=t2, font=s).place(x=634, y=240, width=150, height=30)

           ttk.Button(login,text="Login", command=call_login).place(x=550, y=290, width=250, height=30)



           login.after(1000,voiceG)
           login.mainloop()



