from tkinter import *
from tkinter import  ttk,font
import Teacher_section
import pymysql

def call_display():
    dis_play = Tk()
    dis_play.title("Student's result")
    dis_play.state("zoomed")

    v = font.Font(family="Poppins", size=14, weight="bold")
    s = font.Font(family="Poppins", size=12)

    style = ttk.Style()
    style.configure("TButton", font=("Poppiins", 10))

    def back() :
           dis_play.destroy()
           Teacher_section.t_Desk()

    b = []
    def fetch_db(v):
        db = pymysql.connect(host="localhost", user="root", password="Vaibhav123@", database="college_database")
        sql = "select Class_test.roll_no,Students.name,Class_test.ct_1,Class_test.ct_2 ,avg((Class_test.ct_1+Class_test.ct_2)/2) as avg_marks from Class_test inner join Students on Students.roll_no = Class_test.roll_no where ((Class_test.ct_1+Class_test.ct_2)/2)>7  group by Class_test.roll_no,Students.name;"
        sql2 = "select Class_test.roll_no,Students.name,Class_test.ct_1,Class_test.ct_2 ,avg((Class_test.ct_1+Class_test.ct_2)/2) as avg_marks from Class_test inner join Students on Students.roll_no = Class_test.roll_no where ((Class_test.ct_1+Class_test.ct_2)/2)<=7  group by Class_test.roll_no,Students.name;"
        cur = db.cursor()
        l = 200

        def destroyer():
              for f in b :
                    f[0].destroy()
                    f[1].destroy()
                    f[2].destroy()
                    f[3].destroy()

        if v == "pass":
            if cur.execute(sql):
                destroyer()
                for f in cur.fetchall() :
                     l = l + 32
                     t=ttk.Label(text=f"{f[0]}", font=s)
                     t.place(x=410, y=l, width=20, height=30)
                     u=ttk.Label(text=f"{f[1]}", font=s)
                     u.place(x=512, y=l, width=130, height=30)
                     v=ttk.Label(text=f"{f[2]}", font=s)
                     v.place(x=695, y=l, width=20, height=30)
                     w=ttk.Label(text=f"{f[3]}", font=s)
                     w.place(x=835, y=l, width=20, height=30)
                     c = [t,u,v,w]
                     b.append(c)


        else:
            if cur.execute(sql2):
                    destroyer()
                    for f in cur.fetchall():
                        l = l + 32
                        t = ttk.Label(text=f"{f[0]}", font=s)
                        t.place(x=410, y=l, width=20, height=30)
                        u = ttk.Label(text=f"{f[1]}", font=s)
                        u.place(x=512, y=l, width=130, height=30)
                        v = ttk.Label(text=f"{f[2]}", font=s)
                        v.place(x=695, y=l, width=20, height=30)
                        w = ttk.Label(text=f"{f[3]}", font=s)
                        w.place(x=835, y=l, width=20, height=30)
                        c = [t, u, v, w]
                        b.append(c)

    ttk.Button(text="back to home", command=back).place(x=600, y=70, width=200, height=30)
    ttk.Button(text="Passed Students", command=lambda: fetch_db("pass")).place(x=450, y=150, width=200, height=30)
    ttk.Button(text="Failed Students", command=lambda: fetch_db("fail")).place(x=700, y=150, width=200, height=30)
    ttk.Label(text="Roll no.", font=v).place(x=400, y=200, width=100, height=30)
    ttk.Label(text="Name", font=v).place(x=522, y=200, width=120, height=30)
    ttk.Label(text="Class test-1", font=v).place(x=672, y=200, width=120, height=30)
    ttk.Label(text="Class test-2", font=v).place(x=810, y=200, width=120, height=30)

    dis_play.mainloop()
