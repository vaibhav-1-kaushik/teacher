from tkinter import *
from tkinter import ttk
from tkinter import  font
import pyttsx3
import student_section
import login_teacher


engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def voice() :
    engine.say("welcome to Jhada shera government engineering college ..please proceed")
    engine.runAndWait()

def Students() :
     engine.stop()
     frame.destroy()
     student_section.display()

def Teacher() :
     frame.destroy()
     engine.stop()
     login_teacher.log()

frame = Tk()
frame.title("Engineering college")
v = font.Font(family="Poppins", size=16, weight="bold")
style = ttk.Style()
style.configure("TButton", font=("Poppins"))
frame.state("zoomed")

ttk.Label(text="Jhada Sirha Government Engineering College", font=v).place(x=440, y=150, width=500, height=40)

button = ttk.Button(text="Teachers", command=Teacher)
button.place(x=550, y=200, width=250, height=40)
ttk.Button(text="Students", command=Students).place(x=550, y=250, width=250, height=40)

frame.after(1000,voice)
frame.mainloop()
