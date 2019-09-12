from tkinter import *
from tkinter.ttk import *
import sqlite3
def kishor4():
    link = "D:/employeedatabase/"
    db = "kishordata.db"
    conn = sqlite3.connect(link + db)

    def AddEmployee():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        window.configure(bg='skyblue')
        lbl = Label(window, text="ADD IMPORTED GOODS", font=("Algerian", 50))
        lbl.grid(column=0, row=0)

        lbl1 = Label(window, text="Product ID")
        lbl1.grid(column=0, row=1)

        lbl2 = Label(window, text="product Name")
        lbl2.grid(column=0, row=2)

        lbl3 = Label(window, text="company Name")
        lbl3.grid(column=0, row=3)

        lbl5 = Label(window, text="date of mfg")
        lbl5.grid(column=0, row=4)

        lbl6 = Label(window, text="company address")
        lbl6.grid(column=0, row=5)

        lbl7 = Label(window, text="owner details")
        lbl7.grid(column=0, row=6)

        lbl8 = Label(window, text="date of exp")
        lbl8.grid(column=0, row=7)

        lbl9 = Label(window, text="price")
        lbl9.grid(column=0, row=8)

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

        ent7 = Entry(window, width=30)
        ent7.grid(column=1, row=7)

        ent8 = Entry(window, width=30)
        ent8.grid(column=1, row=8)

        def addemployee():
            link = "D:/employeedatabase/"
            db = "kishordata.db"
            conn = sqlite3.connect(link + db)
            try:
                conn.execute('''CREATE TABLE importedgoods
                          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                           Product_ID         INT     NOT NULL,
                           product_name          TEXT     NOT NULL,
                           company_name          TEXT     NOT NULL,
                           Date_of_mfg      date,
                           company_address             CHAR(50),
                           owner_details             CHAR(50),
                           Date_of_exp   date,
                           price    INT);''')

            except:
                pass
            # res = "Welcome to office" + ent.get()
            # print (ent.get())
            val = (ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), ent7.get(),ent8.get())
            sql = "INSERT INTO importedgoods (Product_ID ,product_name,company_name,Date_of_mfg,company_address,owner_details,Date_of_exp ,price ) VALUES (?,?,?,?,?,?,?,?)"
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
        window.configure(bg='skyblue')
        lbl11 = Label(window, text="EMPLOYEE INFORMATION", font=("Algerian", 50))
        lbl11.grid(column=0, row=0)
        lbl12 = Label(window, text="Enter product_id")
        lbl12.grid(column=0, row=1)
        ent12 = Entry(window, width=30)
        ent12.grid(column=1, row=1)

        def clicked():
            window.destroy()
            window1()

        btn = Button(window, text="Back", command=clicked).place(x=400, y=100)

        def view():
            cursor = conn.execute("SELECT * FROM importedgoods")
            details = []
            for row in cursor:
                print(row[1])
                if row[1] == int(ent12.get()):
                    details.append(row)
            print(details)
            lbl01 = Label(window, text="     ")
            lbl01.grid(column=0, row=2)
            lbl01 = Label(window, text="product ID: ", font=("Algerian", 15))
            lbl01.grid(column=1, row=3)
            lbl01 = Label(window, text=details[0][1], font=("Algerian", 15))
            lbl01.grid(column=3, row=3)

            lbl02 = Label(window, text="     ")
            lbl02.grid(column=0, row=3)
            lbl02 = Label(window, text="product Name: ", font=("Algerian", 15))
            lbl02.grid(column=1, row=4)
            lbl02 = Label(window, text=details[0][2], font=("Algerian", 15))
            lbl02.grid(column=3, row=4)

            lbl03 = Label(window, text="     ")
            lbl03.grid(column=0, row=4)
            lbl03 = Label(window, text="company namee: ", font=("Algerian", 15))
            lbl03.grid(column=1, row=5)
            lbl03 = Label(window, text=details[0][3], font=("Algerian", 15))
            lbl03.grid(column=3, row=5)

            lbl04 = Label(window, text="     ")
            lbl04.grid(column=0, row=5)
            lbl04 = Label(window, text="Date of mfg: ", font=("Algerian", 15))
            lbl04.grid(column=1, row=6)
            lbl04 = Label(window, text=details[0][4], font=("Algerian", 15))
            lbl04.grid(column=3, row=6)

            lbl05 = Label(window, text="     ")
            lbl05.grid(column=0, row=6)
            lbl05 = Label(window, text="company address: ", font=("Algerian", 15))
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
            lbl07 = Label(window, text="owner details: ", font=("Algerian", 15))
            lbl07.grid(column=1, row=9)
            lbl07 = Label(window, text=details[0][7], font=("Algerian", 15))
            lbl07.grid(column=3, row=9)

            lbl08 = Label(window, text="     ")
            lbl08.grid(column=1, row=9)
            lbl08 = Label(window, text="date of exp: ", font=("Algerian", 15))
            lbl08.grid(column=1, row=10)
            lbl08 = Label(window, text=details[0][8], font=("Algerian", 15))
            lbl08.grid(column=4, row=10)

            lbl09 = Label(window, text="     ")
            lbl09.grid(column=0, row=10)
            lbl09 = Label(window, text="price: ", font=("Algerian", 15))
            lbl09.grid(column=1, row=11)
            lbl09 = Label(window, text=details[0][9], font=("Algerian", 15))
            lbl09.grid(column=3, row=11)
        btn = Button(window, text="View", command=view).place(x=490, y=100)
        window.mainloop()

    def EditEmployee():
        window = Tk()
        window.title("Employee Database Managemment")
        window.geometry("1520x850")
        window.configure(bg='skyblue')
        lbl = Label(window, text="UPDATE DATA OF IMPORTED GOODS", font=("Algerian", 50))
        lbl.grid(column=0, row=0)

        lbl1 = Label(window, text="Product ID")
        lbl1.grid(column=0, row=1)

        lbl2 = Label(window, text="product Name")
        lbl2.grid(column=0, row=2)

        lbl3 = Label(window, text="company Name")
        lbl3.grid(column=0, row=3)

        lbl5 = Label(window, text="date of mfg")
        lbl5.grid(column=0, row=4)

        lbl6 = Label(window, text="company address")
        lbl6.grid(column=0, row=5)

        lbl7 = Label(window, text="owner details")
        lbl7.grid(column=0, row=6)

        lbl8 = Label(window, text="date of exp")
        lbl8.grid(column=0, row=7)

        lbl9 = Label(window, text="price")
        lbl9.grid(column=0, row=8)

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

        ent7 = Entry(window, width=30)
        ent7.grid(column=1, row=7)

        ent8 = Entry(window, width=30)
        ent8.grid(column=1, row=8)

        def EditEmployee():
            link = "D:/employeedatabase/"
            db = "kishordata"
            conn = sqlite3.connect(link + db)
            val = (ent1.get(), ent2.get(), ent3.get(), ent4.get(), ent5.get(), ent6.get(), ent7.get(),ent8.get())
            sql = "update importedgoods set  Product ID = ?,  product Name = ?, company Name = ?, date of mfg = ?, company address = ?, owner details = ?, date of exp= ?, price = ?, Salary = ? where  =Product ID ? "
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
        window.title("GOODS DETAILS")
        window.geometry("1520x850")
        window.configure(bg='skyblue')
        lbl = Label(window, text=" IMPORTED GOOD DETAILS", font=("Algerian", 60))
        lbl.grid(column=0, row=0)

        lbl2 = Label(window, text="Add imported goods", font=("Time New Romana Bold", 30))
        lbl2.grid(column=0, row=1)

        def clicked():
            window.destroy()
            AddEmployee()

        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=0, row=2)

        lbl3 = Label(window, text="imported goods Information", font=("Time New Romana Bold", 30))
        lbl3.grid(column=0, row=3)

        def clicked():
            window.destroy()
            EmployeeInformation()

        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=0, row=4)

        lbl4 = Label(window, text="Edit imported goods details", font=("Time New Romana Bold", 30))
        lbl4.grid(column=0, row=5)

        def clicked():
            window.destroy()
            EditEmployee()

        btn = Button(window, text="Click", command=clicked)
        btn.grid(column=0, row=6)

        window.mainloop()

    window1()








