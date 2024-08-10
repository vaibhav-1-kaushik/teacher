from tkinter import *
from tkinter import ttk,font
import login_teacher
import pyttsx3
import pymysql


engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def register() :
                reg = Tk()
                reg.title("Registration Teachers")
                reg.state("zoomed")
                v = font.Font(family="Poppins", size=16, weight="bold")
                s = font.Font(family="Poppins", size=10)
                style = ttk.Style()
                style.configure("TButton", font=("Poppins",10))

                #---->variables<-----
                u_id = StringVar()
                name = StringVar()
                phone = StringVar()
                department = StringVar()
                pw = StringVar()
                #---->methods<----
                def voicef() :
                       engine.say("teacher's registration")
                       engine.runAndWait()
                       engine.say("enter data in the given field")
                       engine.runAndWait()
                def check():
                     text =[ "user id","name","mobile number","department","password"]
                     var = [u_id,name,phone,department,pw]
                     v = 0
                     for f in var :
                                if f.get()=="" :
                                     engine.say(f"enter {text[v]}")
                                     engine.runAndWait()
                                     return 0

                                v = v + 1

                def on_register() :
                           val = check()
                           if val != 0 :
                                   db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="college_database")
                                   sql = f"insert into Teacher values(%s,%s,%s,%s,%s)"
                                   sql2 = f"select * from Teacher where u_id = %s"
                                   value = [u_id.get(),name.get(),phone.get(),department.get(),pw.get()]

                                   cur = db.cursor()

                                   if cur.execute(sql2,value[0]) :
                                                       engine.say("already registered")
                                                       engine.runAndWait()

                                   else:
                                       cur.execute(sql,value)
                                       db.commit()
                                       print("register successfully")
                                       engine.say("register successfully")
                                       engine.runAndWait()
                                       u_id.set("")
                                       name.set("")
                                       phone.set("")
                                       department.set("")
                                       pw.set("")
                                       reg.destroy()
                                       login_teacher.log()





                ttk.Label(reg,text="Jhada Sirha Government Engineering College", font=v).place(x=440, y=150, width=500, height=40)
                ttk.Label(reg, text="Teacher's registration ", font=v).place(x=570, y=194, width=250, height=40)

                ttk.Label(reg, text="User_Id", font=s).place(x=550, y=244, width=70, height=30)
                ttk.Label(reg, text=":", font=s).place(x=622, y=244, width=10, height=30)
                ttk.Entry(reg,textvariable=u_id, font=s).place(x=634, y=244, width=150, height=30)

                ttk.Label(reg, text="Name", font=s).place(x=550, y=278, width=70, height=30)
                ttk.Label(reg, text=":", font=s).place(x=622, y=278, width=10, height=30)
                ttk.Entry(reg,textvariable=name, font=s).place(x=634, y=278, width=150, height=30)

                ttk.Label(reg, text="Mobile no.", font=s).place(x=550, y=312, width=70, height=30)
                ttk.Label(reg, text=":", font=s).place(x=622, y=312, width=10, height=30)
                ttk.Entry(reg,textvariable=phone, font=s).place(x=634, y=312, width=150, height=30)

                ttk.Label(reg, text="Department", font=s).place(x=550, y=346, width=70, height=30)
                ttk.Label(reg, text=":", font=s).place(x=622, y=346, width=10, height=30)
                ttk.Entry(reg, textvariable=department,font=s).place(x=634, y=346, width=150, height=30)

                ttk.Label(reg, text="password", font=s).place(x=550, y=380, width=70, height=30)
                ttk.Label(reg, text=":", font=s).place(x=622, y=380, width=10, height=30)
                ttk.Entry(reg, textvariable=pw, font=s).place(x=634, y=380, width=150, height=30)

                ttk.Button(reg,text="Register", command=on_register).place(x=550, y=415, width=100, height=30)
                reg.after(1000, voicef)
                reg.mainloop()
