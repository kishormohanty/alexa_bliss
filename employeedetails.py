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
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        window.configure(bg='lightblue')
        lbl = Label(window, text="ADD EMPLOYEE", font=("Algerian", 50))
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

        def addemployee():
            link = "D:/employeedatabase/"
            db = "kishordata.db"
            conn = sqlite3.connect(link + db)
            try:
                conn.execute('''CREATE TABLE EmployeeTable
                          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           EmployeeID         INT     NOT NULL,
                           FirstName          TEXT     NOT NULL,
                           LastName           TEXT     NOT NULL,
                           DateofBirth       INT,
                           Gender              CHAR(5),
                           Mobileno          INT,
                           Address             CHAR(50),
                           EmployeePosition   CHAR(15),
                           DateofJoining     INT,
                           Salary              INT);''')

            except:
                pass
            # res = "Welcome to office" + ent.get()
            # print (ent.get())
            val = (
                ent1.get(), ent2.get(), ent3.get(), ent4.get(), selected.get(), ent6.get(), ent7.get(), combo.get(),
                ent9.get(),
                ent10.get())
            sql = "INSERT INTO EmployeeTable (EmployeeID,FirstName,LastName,DateofBirth,Gender,Mobileno,Address,EmployeePosition,DateofJoining,Salary) VALUES (?,?,?,?,?,?,?,?,?,?)"
            conn.execute(sql, val);
            conn.commit()

        print("Hi")
        btn = Button(window, text="Click Me", command=addemployee)
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
        window.configure(bg='lightblue')
        lbl11 = Label(window, text="EMPLOYEE INFORMATION", font=("Algerian", 40))
        lbl11.grid(column=5, row=2)
        lbl12 = Label(window, text="Enter mobile number")
        lbl12.grid(column=8, row=3)
        ent12 = Entry(window, width=30)
        ent12.grid(column=8, row=5)

        def clicked():
            window.destroy()
            window1()

        btn = Button(window, text="Back", command=clicked).grid(column=8, row=10)
        def view():
            cursor = conn.execute("SELECT * FROM EmployeeTable")
            details = []
            for row in cursor:
                print(row[6])
                if row[6] == int(ent12.get()):
                    details.append(row)
            print(details)
            lbl01 = Label(window, text="     ")
            lbl01.grid(column=0, row=2)
            lbl01 = Label(window, text="Employee ID: ", font=("Algerian", 15))
            lbl01.grid(column=1, row=3)
            lbl01 = Label(window, text=details[0][1], font=("Algerian", 15))
            lbl01.grid(column=3, row=3)

            lbl02 = Label(window, text="     ")
            lbl02.grid(column=0, row=3)
            lbl02 = Label(window, text="First Name: ", font=("Algerian", 15))
            lbl02.grid(column=1, row=4)
            lbl02 = Label(window, text=details[0][2], font=("Algerian", 15))
            lbl02.grid(column=3, row=4)

            lbl03 = Label(window, text="     ")
            lbl03.grid(column=0, row=4)
            lbl03 = Label(window, text="Last Name: ", font=("Algerian", 15))
            lbl03.grid(column=1, row=5)
            lbl03 = Label(window, text=details[0][3], font=("Algerian", 15))
            lbl03.grid(column=3, row=5)

            lbl04 = Label(window, text="     ")
            lbl04.grid(column=0, row=5)
            lbl04 = Label(window, text="Date of Birth: ", font=("Algerian", 15))
            lbl04.grid(column=1, row=6)
            lbl04 = Label(window, text=details[0][4], font=("Algerian", 15))
            lbl04.grid(column=3, row=6)

            lbl05 = Label(window, text="     ")
            lbl05.grid(column=0, row=6)
            lbl05 = Label(window, text="Gender: ", font=("Algerian", 15))
            lbl05.grid(column=1, row=7)
            lbl05 = Label(window, text=details[0][5], font=("Algerian", 15))
            lbl05.grid(column=3, row=7)

            lbl06 = Label(window, text="     ")
            lbl06.grid(column=0, row=7)
            lbl06 = Label(window, text="Mobile no: ", font=("Algerian", 15))
            lbl06.grid(column=1, row=8)
            lbl06 = Label(window, text=details[0][6], font=("Algerian", 15))
            lbl06.grid(column=3, row=8)

            lbl07 = Label(window, text="     ")
            lbl07.grid(column=0, row=8)
            lbl07 = Label(window, text="Address: ", font=("Algerian", 15))
            lbl07.grid(column=1, row=9)
            lbl07 = Label(window, text=details[0][7], font=("Algerian", 15))
            lbl07.grid(column=3, row=9)

            lbl08 = Label(window, text="     ")
            lbl08.grid(column=1, row=9)
            lbl08 = Label(window, text="Employee Position: ", font=("Algerian", 15))
            lbl08.grid(column=1, row=10)
            lbl08 = Label(window, text=details[0][8], font=("Algerian", 15))
            lbl08.grid(column=3, row=10)

            lbl09 = Label(window, text="     ")
            lbl09.grid(column=0, row=10)
            lbl09 = Label(window, text="Date of Joining: ", font=("Algerian", 15))
            lbl09.grid(column=1, row=11)
            lbl09 = Label(window, text=details[0][9], font=("Algerian", 15))
            lbl09.grid(column=3, row=11)

            lbl010 = Label(window, text="     ")
            lbl010.grid(column=0, row=11)
            lbl010 = Label(window, text="Salary: ", font=("Algerian", 15))
            lbl010.grid(column=1, row=12)
            lbl010 = Label(window, text=details[0][10], font=("Algerian", 15))
            lbl010.grid(column=3, row=12)

        btn = Button(window, text="View", command=view).grid(column=8, row=7)
        window.mainloop()

    def EditEmployee():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        window.configure(bg='lightblue')
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
        window.mainloop()

    def window1():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        window.configure(bg='lightblue')
        lbl = Label(window, text="   Employee Database Management", font=("Algerian", 40))
        lbl.grid(column=4, row=0)
        lbl2 = Label(window, text="Add Employee", font=("Time New Romana Bold", 30))
        lbl2.grid(column=4, row=3)
        '''def clicked123():
            adminlogin.admlog()
        img123= PhotoImage(file=r"D:\factory ms\log.png")
        img124 = img123.subsample(6, 6)
        btn123= Button(window, text="LOG_OUT",image=img124, command=clicked123)
        btn123.grid(column=10, row=4)'''
        def clicked():
            window.destroy()
            AddEmployee()
        btn = Button(window, text="CLICK ME",command=clicked)
        btn.grid(column=4, row=4)
        lbl3 = Label(window, text="Employee Information", font=("Time New Romana Bold", 30))
        lbl3.grid(column=4, row=5)
        def clicked1():
            window.destroy()
            adminpage.x2()
        btn = Button(window, text="BACK", command=clicked1)
        btn.grid(column=7, row=7)
        def clicked():
            window.destroy()
            EmployeeInformation()
        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=4, row=6)
        lbl4 = Label(window, text="Edit Employee", font=("Time New Romana Bold", 30))
        lbl4.grid(column=4, row=7)
        def clicked():
            window.destroy()
            EditEmployee()
        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=4, row=8)
        window.mainloop()
    window1()








