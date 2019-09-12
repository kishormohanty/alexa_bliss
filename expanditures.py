from tkinter import *
from tkinter.ttk import *
import sqlite3
import adminpage
def kishor1():
    link = "D:/employeedatabase/"
    db = "kishordata.db"
    conn = sqlite3.connect(link + db)

    def AddEmployee():
        window = Tk()
        window.title("EXPANDITURES")
        window.geometry("1520x850")
        window.configure(bg='lightblue')
        lbl = Label(window, text="ADD DETAILS", font=("Algerian", 50))
        lbl.grid(column=0, row=0)

        lbl1 = Label(window, text="DATE")
        lbl1.grid(column=0, row=1)

        lbl2 = Label(window, text="NO_OF_PRODUCT_IMPORTED")
        lbl2.grid(column=0, row=2)

        lbl3 = Label(window, text="NO_OF_PRODUCT_EXPORTED")
        lbl3.grid(column=0, row=3)

        lbl4 = Label(window, text="PROFIT")
        lbl4.grid(column=0, row=4)

        lbl6 = Label(window, text="LOSS")
        lbl6.grid(column=0, row=5)

        lbl7 = Label(window, text="NO_OF_MFG")
        lbl7.grid(column=0, row=6)

        ent1 = Entry(window, width=30)
        ent1.grid(column=1, row=1)

        ent2 = Entry(window, width=30)
        ent2.grid(column=1, row=2)

        ent3 = Entry(window, width=30)
        ent3.grid(column=1, row=3)

        ent4 = Entry(window, width=30)
        ent4.grid(column=1, row=4)

        ent5 = Entry(window, width=30)
        ent5.grid(column=1, row=5)

        ent6 = Entry(window, width=30)
        ent6.grid(column=1, row=6)
        def h3():
            link = "D:/employeedatabase/"
            db = "kishordata.db"
            conn = sqlite3.connect(link + db)
            try:
                conn.execute('''CREATE TABLE EXPANDITURES
                          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           DATE        DATE    ,
                           NO_OF_PRODUCT_IMPORTED        INT    NOT NULL,
                           NO_OF_PRODUCT_EXPORTED        INT    NOT NULL,
                           PROFIT      INT,
                           LOSS         int,
                           NO OF MFG PRODUCTS   INT,''')
            except:
                pass
            # res = "Welcome to office" + ent.get()
            # print (ent.get())
            val = (ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get())
            sql = "INSERT INTO EXPANDITURES (DATE,NO_OF_PRODUCT_IMPORTED ,NO_OF_PRODUCT_EXPORTED ,PROFIT , LOSS ,NO OF MFG PRODUCTS   ) VALUES (?,?,?,?,?,?)"
            conn.execute(sql, val);
            conn.commit()
        btn = Button(window, text="Click Me", command=h3)
        btn.grid(column=1, row=12)
        def clicked():
            window.destroy()
            window1()

        btn = Button(window, text="Back", command=clicked)
        btn.grid(column=0, row=13)
        window.mainloop()

    def EmployeeInformation():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        lbl11 = Label(window, text="EMPLOYEE INFORMATION", font=("Algerian", 50))
        lbl11.grid(column=0, row=0)
        lbl12 = Label(window, text="DATE")
        lbl12.grid(column=0, row=1)
        ent12 = Entry(window, width=30)
        ent12.grid(column=1, row=1)

        def clicked():
            window.destroy()
            window1()

        btn = Button(window, text="Back", command=clicked).place(x=400, y=100)

        def view():
            cursor = conn.execute("SELECT * FROM EXPANDITURES ")
            details = []
            for row in cursor:
                print(row[1])
                if row[1] == int(ent12.get()):
                    details.append(row)
            print(details)
            lbl01 = Label(window, text="     ")
            lbl01.grid(column=0, row=2)
            lbl01 = Label(window, text="DATE: ", font=("Algerian", 15))
            lbl01.grid(column=1, row=3)
            lbl01 = Label(window, text=details[0][1], font=("Algerian", 15))
            lbl01.grid(column=3, row=3)

            lbl02 = Label(window, text="     ")
            lbl02.grid(column=0, row=3)
            lbl02 = Label(window, text="NO_OF_IMPORTED_GOODS: ", font=("Algerian", 15))
            lbl02.grid(column=1, row=4)
            lbl02 = Label(window, text=details[0][2], font=("Algerian", 15))
            lbl02.grid(column=3, row=4)

            lbl03 = Label(window, text="     ")
            lbl03.grid(column=0, row=4)
            lbl03 = Label(window, text="NO_OF_EXPORTED_GOODS: ", font=("Algerian", 15))
            lbl03.grid(column=1, row=5)
            lbl03 = Label(window, text=details[0][3], font=("Algerian", 15))
            lbl03.grid(column=3, row=5)

            lbl04 = Label(window, text="     ")
            lbl04.grid(column=0, row=5)
            lbl04 = Label(window, text="PROFIT: ", font=("Algerian", 15))
            lbl04.grid(column=1, row=6)
            lbl04 = Label(window, text=details[0][4], font=("Algerian", 15))
            lbl04.grid(column=3, row=6)

            lbl05 = Label(window, text="     ")
            lbl05.grid(column=0, row=6)
            lbl05 = Label(window, text="LOSS: ", font=("Algerian", 15))
            lbl05.grid(column=1, row=7)
            lbl05 = Label(window, text=details[0][5], font=("Algerian", 15))
            lbl05.grid(column=3, row=7)

            lbl06 = Label(window, text="     ")
            lbl06.grid(column=0, row=7)
            lbl06 = Label(window, text="NO_OF_MFG_GOODS: ", font=("Algerian", 15))
            lbl06.grid(column=1, row=8)
            lbl06 = Label(window, text=details[0][6], font=("Algerian", 15))
            lbl06.grid(column=3, row=8)
        btn = Button(window, text="View", command=view).place(x=490, y=100)
        window.mainloop()
    '''def EditEmployee():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        lbl = Label(window, text="EDIT EMPLOYEE", font=("Algerian", 50))
        lbl.grid(column=0, row=0)

        lbl1 = Label(window, text="Employee ID")
        lbl1.grid(column=0, row=1)

        lbl2 = Label(window, text="First Name")
        lbl2.grid(column=0, row=2)

        lbl3 = Label(window, text="Last Name")
        lbl3.grid(column=0, row=3)

        lbl4 = Label(window, text="Date of Birth")
        lbl4.grid(column=0, row=4)

        lbl5 = Label(window, text="Gender")
        lbl5.grid(column=0, row=5)
        selected = IntVar()
        rad1 = Radiobutton(window, text='Male', value=1, variable=selected)
        rad2 = Radiobutton(window, text='Female', value=2, variable=selected)
        rad1.grid(column=1, row=5)
        rad2.grid(column=2, row=5)

        lbl6 = Label(window, text="Mobile no.")
        lbl6.grid(column=0, row=6)

        lbl7 = Label(window, text="Address")
        lbl7.grid(column=0, row=7)

        lbl8 = Label(window, text="Employee Position")
        lbl8.grid(column=0, row=8)
        combo = Combobox(window)
        combo['values'] = (
            "Select", "ceo", "VP", "Manager", "Senior-Associate", "Technical-Analyst", "Team-Leader",
            "Senior-Developer",
            "Junior-Devloper")
        combo.current(0)
        combo.grid(column=1, row=8)

        lbl9 = Label(window, text="Date of Joining")
        lbl9.grid(column=0, row=9)

        lbl10 = Label(window, text="Salary")
        lbl10.grid(column=0, row=10)

        ent1 = Entry(window, width=30)
        ent1.grid(column=1, row=1)

        ent2 = Entry(window, width=30)
        ent2.grid(column=1, row=2)

        ent3 = Entry(window, width=30)
        ent3.grid(column=1, row=3)

        ent4 = Entry(window, width=30)
        ent4.grid(column=1, row=4)

        ent6 = Entry(window, width=30)
        ent6.grid(column=1, row=6)

        ent7 = Entry(window, width=30)
        ent7.grid(column=1, row=7)

        ent9 = Entry(window, width=30)
        ent9.grid(column=1, row=9)

        ent10 = Entry(window, width=30)
        ent10.grid(column=1, row=10)

        def EditEmployee():
            link = "D:/employeedatabase/"
            db = "kishordata"
            conn = sqlite3.connect(link + db)

            val = (ent1.get(), ent2.get(), ent3.get(), ent4.get(), selected.get(), ent10.get(), ent7.get(), combo.get(),
                   ent9.get(), ent6.get())
            sql = "update EmployeeTable set  EmployeeID = ?,  FirstName = ?, LastName = ?, DateofBirth = ?, Gender = ?, Address = ?, EmployeePosition = ?, DateofJoining = ?, Salary = ? where Mobileno = ? "
            conn.execute(sql, val);
            conn.commit()

        btn = Button(window, text="Submit", command=EditEmployee)
        btn.grid(column=1, row=12)

        def back():
            window.destroy()
            window1()

        btn = Button(window, text="Back", command=back)
        btn.grid(column=0, row=13)
        window.mainloop()'''

    def window1():
        window = Tk()
        window.title("EXPANDITURES OF GIET FACTORY")
        window.geometry("1520x850")
        window.configure(bg='lightblue')
        lbl = Label(window, text="   EXPANDITURES OF GIET FACTORY", font=("Algerian", 40))
        lbl.grid(column=4, row=0)
        lbl2 = Label(window, text="ADD EXPANDITURES", font=("Time New Romana Bold", 30))
        lbl2.grid(column=4, row=3)
        def clicked():
            window.destroy()
            AddEmployee()
        btn = Button(window, text="CLICK ME",command=clicked)
        btn.grid(column=4, row=4)
        lbl3 = Label(window, text="SHOW EXPANDITURES", font=("Time New Romana Bold", 30))
        lbl3.grid(column=4, row=5)
        def clicked1():
            window.destroy()
        btn = Button(window, text="BACK", command=clicked1)
        btn.grid(column=7, row=7)
        def clicked():
            window.destroy()
            EmployeeInformation()
        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=4, row=6)
        window.mainloop()
    window1()








