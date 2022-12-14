from tkinter import *
import customtkinter as ctk
import awesometkinter as atk

from login import login_func

def elployeeprofile_func(id,name, email, phone, salary, pic, self):

    screen_height = 350
    screen_width = 500

    employee_profile = Toplevel()
    employee_profile.geometry('500x350')
    employee_profile.resizable(False, False)
    employee_profile.configure(bg='black')
    employee_profile.title('Employees')



    ######################## FRAME 1 ############################
    frame1 = Frame(employee_profile,height=screen_height *0.25, width= screen_width, bg= '#3b1c47')
    frame1.pack(side=TOP,  fill = BOTH, expand= YES)

    username = Label(frame1, text=name, fg = '#22eba3', bg = '#3b1c47', font=('Arial',30))
    username.place(x=screen_width * 0.45, y=screen_height * 0.06)

    def back_func():
        employee_profile.destroy()
        self.deiconify()

    back_icon = PhotoImage(file=r"assets/Back_PNG.png")
    back_icon =back_icon.zoom(1)
    back_icon =back_icon.subsample(70)
    back_btn = Button(frame1 ,image=back_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47', command = back_func)
    back_btn.place(x=screen_width * 0.92, y=screen_height * 0.04)



    ######################## FRAME 2 ############################
    frame2 = Frame(employee_profile,height=screen_height *0.75, width= screen_width, bg= 'black')
    frame2.pack(side=BOTTOM, fill = BOTH, expand= YES,)

    logo_path = PhotoImage(file='assets/SMALL_Iress_Logo.png')
    logo_path = logo_path.zoom(1)
    logo_path = logo_path.subsample(15)
    logo = Label(frame2, image= logo_path, width= screen_height * 0.25 , height= screen_height * 0.25, bg = 'black')
    logo.place(x=screen_width * 0.1, y=screen_height * 0.4)

    email_icon_path = PhotoImage(file='assets/Email_PNG.png')
    email_icon_path = email_icon_path.zoom(1)
    email_icon_path = email_icon_path.subsample(55)
    email_icon = Label(frame2, image= email_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    email_icon.place(x=screen_width * 0.35, y=screen_height * 0.05)

    useremail = Label(frame2, text=email, fg = '#22eba3', bg = 'black', font=('Arial',16))
    useremail.place(x=screen_width * 0.45, y=screen_height * 0.06)

    phone_icon_path = PhotoImage(file='assets/Phone_PNG.png')
    phone_icon_path = phone_icon_path.zoom(1)
    phone_icon_path = phone_icon_path.subsample(55)
    phone_icon = Label(frame2, image= phone_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    phone_icon.place(x=screen_width * 0.35, y=screen_height * 0.21)

    useremail = Label(frame2, text=phone, fg = '#22eba3', bg = 'black', font=('Arial',16))
    useremail.place(x=screen_width * 0.45, y=screen_height * 0.22)

    # salary_icon_path = PhotoImage(file='assets/Salary_PNG.png')
    # salary_icon_path = salary_icon_path.zoom(1)
    # salary_icon_path = salary_icon_path.subsample(55)
    # salary_icon = Label(frame2, image= salary_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    # salary_icon.place(x=screen_width * 0.35, y=screen_height * 0.36)

    # usersalary = Label(frame2, text=salary, fg = '#22eba3', bg = 'black', font=('Arial',16))
    # usersalary.place(x=screen_width * 0.45, y=screen_height * 0.37)

    def edit_func():
        login_func(id,name, email, phone, salary,pic,isedit=True, isnewuser=False)
        # ctk.CTkInputDialog(master=frame2, title='Authenticate',text='Login')
        # print(atk.dialog.filechooser(initialdir='assets/'))

    edit_btn = Button(frame2, text='Edit', bg='#3b1c47',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',15),padx=15, command=edit_func)
    edit_btn.place(x=screen_width * 0.55, y=screen_height * 0.5)

    # profile_pic_path = PhotoImage(data=pic)
    # profile_pic_path = profile_pic_path.zoom(1)
    # profile_pic_path = profile_pic_path.subsample(1)
    profile_pic = Label(employee_profile, image= pic, bg = '#3b1c47')
    profile_pic.place(x=screen_width * 0.03, y=screen_height * 0.03)

    employee_profile.mainloop()