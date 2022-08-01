from tkinter import *
import customtkinter as ctk

def login_func():

    screen_height = 250
    screen_width = 400

    login = Toplevel()
    login.geometry('400x250')
    login.resizable(False, False)
    login.configure(bg='black')
    # login.title('Employees')

    ######################## FRAME 1 ############################
    frame1 = Frame(login, height=screen_height *0.1, width= screen_width, bg= '#3b1c47')
    frame1.pack(side=TOP,  fill = BOTH, expand= YES)


    username = Label(frame1, text='Authenticate', fg = '#22eba3', bg = '#3b1c47', font=('Arial',16))
    username.place(x=screen_width * 0.35, y=screen_height * 0.04)

    edit_icon = PhotoImage(file=r"assets/Back_PNG.png")
    edit_icon =edit_icon.zoom(1)
    edit_icon =edit_icon.subsample(70)
    edit_btn = Button(frame1 ,image=edit_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47')
    edit_btn.place(x=screen_width * 0.92, y=screen_height * 0.04)

    ######################## FRAME 2 ############################
    frame2 = Frame(login,height=screen_height *0.8, width= screen_width, bg= 'black')
    frame2.pack(side=BOTTOM, fill = BOTH, expand= YES,)

    passvar = StringVar()
    passvar.set('Password')


    pass_input = Entry(master=frame2,textvariable=passvar,fg='black',relief=FLAT, bg='grey')
    pass_input.place(x=screen_width * 0.37, y=screen_height * 0.3)
    login_btn = Button(frame2, text='Login', bg='#3b1c47',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',13),padx=10)
    login_btn.place(x=screen_width * 0.42, y=screen_height * 0.45)

    login.mainloop()