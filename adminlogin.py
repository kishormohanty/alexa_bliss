from tkinter import *
import sqlite3
import adminpage
#import home
def admlog():
    windows = Tk()
    windows.title("EMPLOYEE")
    windows.geometry('2000x2000')
    windows.configure(bg='lightblue')

    def c2():
        win = Tk()
        win.title("widget-2")
        win.geometry('3000x3000')
        win.configure(bg='lightblue')
        lb = Label(win, text="USER_ID")
        lb.place(x=500, y=200)
        pss = Entry(win, width=30)
        pss.place(x=600, y=200)
        lb1 = Label(win, text="PASSWARD")
        lb1.place(x=500, y=300)
        pss1 = Entry(win, width=30)
        pss1.place(x=600, y=300)

        def clicked1():
            link = "D:/employeedatabase/"
            db = "kishordata.db"
            conn = sqlite3.connect(link + db)
            try:
                b3 = conn.execute(
                    "select * from user where user_id= '" + pss.get() + "' and passward= '" + pss1.get() + "'")
                print("select * from user where user_id= '" + pss.get() + "' and passward= '" + pss1.get() + "'")
                print('welcome')
            except Exception as e:
                print('invalid', e)

                '''if row[0] == pss.get() and row[1] == pss1.get():
                    print("next page valid")
                    break
                else:
                    print("not valid.....")'''

        def x3():
            win.destroy()
            adminpage.x2()
        btn = Button(win, text='SIGN IN', command=x3)
        btn.place(x=600, y=400)
        '''def c4():
            win.destroy()
            home.vinay()
        btnqw = Button(win, text='BACK', command=c4)
        btnqw.place(x=600, y=450)'''
        windows.destroy()
        win.mainloop()
    img = PhotoImage(file=r"D:\factory ms\s.png")
    img1 = img.subsample(2,2)
    btn = Button(windows,text="            SIGN_IN                         " ,image=img1,compound=LEFT, command=c2)
    btn.place(x=820, y=330)
    def c1():
        window = Tk()
        window.title("signup screen")
        window.geometry('3000x3000')
        window.configure(bg='lightblue')
        link = "D:/employeedatabase/"
        db = "user.db"
        conn = sqlite3.connect(link + db)
        lb1= Label(window, text="USER_ID")
        lb1.place(x=100, y=100)
        pss = Entry(window, width=30)
        pss.place(x=200, y=100)
        '''img12=PhotoImage(file=r"D:\factory ms\passward.png")
        img13=img11.subsample(3,3'''
        lb2=Label(window, text="PASSWORD")
        lb2.place(x=100, y=150)
        pss1 = Entry(window, width=30)
        pss1.place(x=200, y=150)

        def back():
            window.destroy()
            c2()

        def clicked():
            try:
                conn.execute('''CREATE TABLE user (user_id varchar(50),passward varchar(50)) ''')
            except:
                pass
            val = (
                pss.get(), pss1.get())
            sql = "INSERT INTO user (user_id,passward) VALUES (?,?)"
            conn.execute(sql, val);
            conn.commit()

        btn = Button(window, text='SIGN UP', command=clicked)
        btn.place(x=190, y=250)
        btn1 = Button(window, text='BACK', command=back)
        btn1.place(x=190, y=300)
        windows.destroy()
        window.mainloop()

    img2 = PhotoImage(file=r"D:\factory ms\s.png")
    img3 = img.subsample(2, 2)
    btn = Button(windows,text="     CREATE NEW ADMIN     ",image=img3,compound=LEFT, command=c1)
    btn.place(x=320, y=330)
    windows.mainloop()
