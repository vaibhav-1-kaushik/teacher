from tkinter import *
from  tkinter import ttk,font
import Teacher_section
import pymysql
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def S_reg() :
    st = Tk()
    st.title("Student registration")
    st.state("zoomed")
    v = font.Font(family="Poppins", size=16, weight="bold")
    s = font.Font(family="Poppins", size=10)
    style = ttk.Style()
    style.configure("TButton", font=("Poppins", 10))
    # ----->variables<-----
    roll_ = StringVar()
    name_ = StringVar()
    phone_ = StringVar()
    branch_ = StringVar()
    semester_ = StringVar()
    email_ = StringVar()
    def entry() :
         engine.say("enter values for given filed")
         engine.runAndWait()

    def check():
        text = ["Roll number", "name", "mobile number", "branch", "semester", "e mail"]
        var = [roll_, name_, phone_, branch_, semester_, email_]
        v = 0
        for f in var:

            if f.get() == "":
                engine.say(f"enter {text[v]}")
                engine.runAndWait()
                return 0

            v = v + 1


    def database_() :
          d_v = check()
          if d_v != 0 :
                   db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="college_database")
                   sql = " insert into Students values(%s,%s,%s,%s,%s,%s)"
                   sql2 = "select * from Students where roll_no = %s"
                   value = [roll_.get(),name_.get(),phone_.get(),branch_.get(),semester_.get(),email_.get()]

                   cur = db.cursor()
                   if cur.execute(sql2,value[0]) :
                           engine.say("student is already register")
                           engine.runAndWait()

                   else :
                       cur.execute(sql,value)
                       db.commit()
                       engine.say("Save successfully")
                       engine.runAndWait()
                       roll_.set("")
                       name_.set("")
                       phone_.set("")
                       semester_.set("")
                       branch_.set("")
                       email_.set("")
                       st.destroy()
                       Teacher_section.t_Desk()



    ttk.Label(st, text="Jhada Sirha Government Engineering College", font=v).place(x=440, y=150, width=500, height=40)
    ttk.Label(st, text="Student's registration ", font=v).place(x=570, y=194, width=250, height=40)

    ttk.Label(st, text="Roll no.", font=s).place(x=550, y=244, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=244, width=10, height=30)
    ttk.Entry(st,textvariable=roll_, font=s).place(x=634, y=244, width=150, height=30)

    ttk.Label(st, text="Name", font=s).place(x=550, y=278, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=278, width=10, height=30)
    ttk.Entry(st,textvariable=name_,font=s).place(x=634, y=278, width=150, height=30)

    ttk.Label(st, text="Mobile no.", font=s).place(x=550, y=312, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=312, width=10, height=30)
    ttk.Entry(st, textvariable=phone_,font=s).place(x=634, y=312, width=150, height=30)

    ttk.Label(st, text="Branch", font=s).place(x=550, y=346, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=346, width=10, height=30)
    ttk.Entry(st,textvariable=branch_, font=s).place(x=634, y=346, width=150, height=30)

    ttk.Label(st, text="Semester", font=s).place(x=550, y=380, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=380, width=10, height=30)
    ttk.Entry(st,textvariable=semester_ ,font=s).place(x=634, y=380, width=150, height=30)

    ttk.Label(st, text="E-Mail", font=s).place(x=550, y=414, width=70, height=30)
    ttk.Label(st, text=":", font=s).place(x=622, y=414, width=10, height=30)
    ttk.Entry(st, textvariable=email_,font=s).place(x=634, y=414, width=150, height=30)


    ttk.Button(st,text="save", command=database_).place(x=585, y=448, width=150, height=30)
    st.after(1000,entry)

    st.mainloop()

