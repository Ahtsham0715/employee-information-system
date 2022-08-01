from asyncio.windows_events import NULL
from tkinter import *
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import awesometkinter as atk

from employees import employees_func

# from employees import employees_func

def adduser_func():

    screen_height = 350
    screen_width = 500

    adduser = Toplevel()
    adduser.geometry('500x350')
    adduser.resizable(False, False)
    adduser.configure(bg='black')
    adduser.title('Add Employee')



    ######################## FRAME 1 ############################
    frame1 = Frame(adduser,height=screen_height *0.25, width= screen_width, bg= '#3b1c47')
    frame1.pack(side=TOP,  fill = BOTH, expand= YES)

    username = Label(frame1, text='Add Employee', fg = '#22eba3', bg = '#3b1c47', font=('Arial',20))
    username.place(x=screen_width * 0.5, y=screen_height * 0.07)

    def back_func():
        adduser.destroy()
        employees_func()

    back_icon = PhotoImage(file=r"assets/Back_PNG.png")
    back_icon =back_icon.zoom(1)
    back_icon =back_icon.subsample(70)
    back_btn = Button(frame1 ,image=back_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47', command=back_func)
    back_btn.place(x=screen_width * 0.92, y=screen_height * 0.04)



    ######################## FRAME 2 ############################
    frame2 = Frame(adduser,height=screen_height *0.75, width= screen_width, bg= 'black')
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

    useremailvar = StringVar()
    useremail = Entry(frame2, textvariable=useremailvar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    useremail.place(x=screen_width * 0.45, y=screen_height * 0.05)

    phone_icon_path = PhotoImage(file='assets/Phone_PNG.png')
    phone_icon_path = phone_icon_path.zoom(1)
    phone_icon_path = phone_icon_path.subsample(55)
    phone_icon = Label(frame2, image= phone_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    phone_icon.place(x=screen_width * 0.35, y=screen_height * 0.21)

    userphonevar = StringVar()
    userphone = Entry(frame2, textvariable=userphonevar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    userphone.place(x=screen_width * 0.45, y=screen_height * 0.21)

    salary_icon_path = PhotoImage(file='assets/Salary_PNG.png')
    salary_icon_path = salary_icon_path.zoom(1)
    salary_icon_path = salary_icon_path.subsample(55)
    salary_icon = Label(frame2, image= salary_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    salary_icon.place(x=screen_width * 0.35, y=screen_height * 0.36)

    usersalaryvar = StringVar()
    usersalary = Entry(frame2, textvariable=usersalaryvar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    usersalary.place(x=screen_width * 0.45, y=screen_height * 0.36)

    isimageselected = False

    def submit_func():
        if(len(useremailvar.get()) == 0 or len(userphonevar.get()) == 0 or len(usersalaryvar.get()) == 0):
            messagebox.showerror('Error', 'Please fill all fields')
        else:
            if isimageselected == False:
                messagebox.showerror('Error', 'Please Select Profile Picture')
            else:
                pass
    submit_btn = Button(frame2, text='Submit', bg='#3b1c47',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',15),padx=15, command=submit_func)
    submit_btn.place(x=screen_width * 0.55, y=screen_height * 0.6)

    imgpath = PhotoImage(file='assets/dummy_icon.png')
    imgpath = imgpath.zoom(1)
    imgpath = imgpath.subsample(1)
    profile_pic = Label(adduser, image= imgpath, width= screen_height * 0.4 , height= screen_height * 0.55, bg = '#3b1c47')
    profile_pic.place(x=screen_width * 0.03, y=screen_height * 0.03)  


    def img_func():
        global imgpath, isimageselected
        imgpath = atk.dialog.filechooser(initialdir='assets/')
        print(imgpath)
        # print(str(imgpath).split('/')[5] + '/' + str(imgpath).split('/')[6])
        if not imgpath == '':
            isimageselected = True
            profile_pic_path = PhotoImage(file=imgpath)
            profile_pic_path = profile_pic_path.zoom(1)
            profile_pic_path = profile_pic_path.subsample(1)
            imgpath=profile_pic_path
            profile_pic.config(image=imgpath)
            # select_btn['state'] = DISABLED
        else:
            imgpath = PhotoImage(file='assets/dummy_icon.png')
            imgpath = imgpath.zoom(1)
            imgpath = imgpath.subsample(1)
            profile_pic.config(image=imgpath)
            


    select_btn = Button(frame2, text='Select Image', bg='black',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',8), command=img_func)
    select_btn.place(x=screen_width * 0.8, y=screen_height * 0.5)



    adduser.mainloop()
    
# adduser_func()