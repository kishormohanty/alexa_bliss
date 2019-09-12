from tkinter import *
import importedgoods
import exportedgoods
def x1():
    windows = Tk()
    windows.title(".............employee.............")
    windows.geometry('2000x3600')
    windows.configure(bg='lightblue')
    def kishor3():
        importedgoods.kishor4()
    def kishor5():
        exportedgoods.kishor6()
    img = PhotoImage(file=r"D:\factory ms\goods.png")
    img1 = img.subsample(4, 4)
    img2 = PhotoImage(file=r"D:\factory ms\adm.png")
    img3 = img.subsample(4, 4)
    btn = Button(windows, text="IMPORTED GOODS",image=img1,compound=LEFT ,command=kishor3)
    btn.place(x=320,y=330)
    btn = Button(windows, text="EXPORTED GOODS", image=img3,compound=LEFT,command=kishor5)
    btn.place(x=920, y=330)
    windows.mainloop()



