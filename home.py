from tkinter import *
from tkinter.ttk import *
import adminlogin as adlg
import employeelogin as emlg
import tkinter as tk
import tkinter as sk
import webbrowser as wb
from time import strftime
windows=Tk()
windows.title(".............GIET FACTORY.............")
windows.geometry('2000x2000')
windows.configure(bg='lightblue')
lb=Label(windows,text='GIET FACTORY',font=("Helvetica", 40,))
lb.place(x=450,y=90)
def time():
    string = strftime('%H:%M:%S %p')
    lbl9.config(text = string)
    lbl9.after(1000, time)
lbl9 = Label(windows, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
lbl9.pack(anchor = 'nw')
time()
def adm():
    windows.destroy()
    adlg.admlog()
def emp():
    windows.destroy()
    emlg.emplg()
img=PhotoImage(file = r"D:\factory ms\emp.png")
img1=img.subsample(3,3)
img2=PhotoImage(file = r"D:\factory ms\adm.png")
img3=img.subsample(3,3)
btn=Button(windows,text='EMPLOYEE',image =img1,compound=LEFT,command=emp)
btn.place(x=320,y=330)
btn1=Button(windows,text='ADMIN',image=img3,compound=LEFT,command=adm)
btn1.place(x=820,y=330)
def m2():
    root = tk.Tk()
    T = tk.Text(root, height=1000, width=1000)
    T.pack()
    quote = """HAMLET: To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummation
    Devoutly to be wished.AMLET: To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummationAMLET: To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummationAMLET: To be, or not to be--that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune
    Or to take arms against a sea of troubles
    And by opposing end them. To die, to sleep--
    No more--and by a sleep to say we end
    The heartache, and the thousand natural shocks
    That flesh is heir to. 'Tis a consummation"""
    T.insert(tk.END, quote)
    tk.mainloop()
img30=PhotoImage(file = r"D:\factory ms\about.png")
img31=img30.subsample(3,3)
btn5=Button(windows,image=img31,command=m2)
btn5.place(x=1250,y=0)
def m3():
    root1 = sk.Tk()
    T1= sk.Text(root1, height=1000, width=1000)
    T1.pack()
    quote = """HAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation
        Devoutly to be wished.AMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummationAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummationAMLET: To be, or not to be--that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune
        Or to take arms against a sea of troubles
        And by opposing end them. To die, to sleep--
        No more--and by a sleep to say we end
        The heartache, and the thousand natural shocks
        That flesh is heir to. 'Tis a consummation"""
    T1.insert(sk.END, quote)
    sk.mainloop()
img26=PhotoImage(file = r"D:\factory ms\contact.png")
img27=img26.subsample(3,3)
btna=Button(windows,image=img27,command=m3)
btna.place(x=1250,y=100)
img20=PhotoImage(file = r"D:\factory ms\fb.png")
img21=img20.subsample(3,3)
img22=PhotoImage(file = r"D:\factory ms\insta.png")
img23=img22.subsample(3,3)
img24=PhotoImage(file = r"D:\factory ms\youtube.png")
img25=img24.subsample(3,3)
def fb():
    wb.open('https://www.facebook.com/kishormohanty.empire11')
btn5=Button(windows,image=img21,command=fb)
btn5.place(x=0,y=450)

def aaa():
    wb.open('www.instagram.com')
btn5=Button(windows,image=img23,command=aaa)
btn5.place(x=0,y=550)
def yo():
    wb.open('www.youtube.com')
btn5=Button(windows,image=img25,command=yo)
btn5.place(x=0,y=650)

windows.mainloop()





