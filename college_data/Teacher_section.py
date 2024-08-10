from tkinter import *
from tkinter import ttk
import Student_registration
import CT_
import dis_result

def t_Desk() :
              sec = Tk()
              sec.title("Teacher's section")
              sec.state("zoomed")
              style = ttk.Style()
              style.configure("TButton", font=("Poppins", 12))

              def S_call() :
                   sec.destroy()
                   Student_registration.S_reg()

              def Ct_ent() :
                    sec.destroy()
                    CT_.C_marks()

              def results() :
                     sec.destroy()
                     dis_result.call_display()

              ttk.Button(sec, text="Add student", command=S_call).place(x=550, y=200, width=150, height=50)
              ttk.Button(sec, text="Class test (CT)", command=Ct_ent).place(x=550, y=255, width=150, height=50)
              ttk.Button(sec, text="Results", command=results).place(x=550, y=310, width=150, height=50)


              sec.mainloop()

