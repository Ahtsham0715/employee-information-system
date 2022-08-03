import sqlite3
from tkinter import *

def home_func():

    conn = sqlite3.connect('employees.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
            (ID INTEGER PRIMARY KEY  AUTOINCREMENT NOT NULL,
            NAME           TEXT    NOT NULL,
            EMAIL            TEXT     NOT NULL,
            PHONE        TEXT,
            SALARY         TEXT,
            IMAGE       TEXT
            );''')
    print ("Table created successfully")
    conn.close()

    screen_height = 350
    screen_width = 500

    home = Tk()
    home.geometry('500x350')
    home.resizable(False, False)
    home.configure(bg='black')
    ######################## FRAME 1 ############################
    frame1 = Frame(home,height=screen_height *0.8, width= screen_width, bg= 'black')
    frame1.pack(side=TOP,  fill = BOTH, expand= YES)

    logo_path = PhotoImage(file='assets/SMALL_Iress_Logo.png')
    logo_path = logo_path.zoom(6)
    logo_path = logo_path.subsample(32)
    logo = Label(frame1, image= logo_path, width= screen_height * 0.7 , height= screen_height * 0.7, bg='black')
    logo.pack(side=LEFT, padx = 10)

    def open_func():
        home.destroy()
        import employees
        employees.employees_func()
    
    open_btn = Button(frame1, text='Open', bg='#3b1c47', fg='white',command=open_func)
    open_btn.pack(side = RIGHT, padx=50, ipadx=15)

    ######################## FRAME 2 ############################
    frame2 = Frame(home,height=screen_height *0.2, width= screen_width, bg= '#3b1c47')
    frame2.pack(side=BOTTOM, fill = BOTH, expand= YES)

    txt0 = Label(frame2, text='', fg = '#22eba3', bg = '#3b1c47', font=(18))
    txt0.pack(anchor='center', side=TOP)

    txt1 = Label(frame2, text='Employee Information', fg = '#22eba3', bg = '#3b1c47', font=('Arial',16))
    txt1.pack(anchor='center', side=TOP)

    txt2 = Label(frame2, text='System', fg = 'white', bg = '#3b1c47', font=('Arial',16,))
    txt2.pack(anchor='center',)

    home.mainloop()

home_func()