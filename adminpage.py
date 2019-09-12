from tkinter import *
import employeedetails
#import showemployee
#import updateemployee
import expanditures
def x2():
    windows = Tk()
    windows.title(".............admin.............")
    windows.geometry('3000x3000')
    windows.configure(bg='lightblue')
    lb = Label(windows, text='WELCOME TO GIET', font=("Helvetica", 40,))
    lb.place(x=450, y=90)
    def kishor():
        windows.destroy()
        employeedetails.kishor1()
    img = PhotoImage(file=r"D:\factory ms\a.png")
    x=img.subsample(4,4)
    btn = Button(windows, text="  EMPLOYEE INFO  ",image=x,compound=LEFT,command=kishor)
    btn.place(x=0, y=210)
    def left():
        expanditures.kishor1()
    img1 = PhotoImage(file=r"D:\factory ms\a.png")
    y = img1.subsample(4, 4)
    btn = Button(windows, text="    EXPANDITURES    ",image=y,compound=LEFT,command=left)
    btn.place(x=0, y=510)
    windows.mainloop()


