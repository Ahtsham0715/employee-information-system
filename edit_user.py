from asyncio.windows_events import NULL
from tkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import awesometkinter as atk
import sqlite3
import base64
selectedimagepath = ''
def edituser_func(id,name, email, phone, salary, pic):

    screen_height = 350
    screen_width = 500

    edituser = Toplevel()
    edituser.geometry('500x350')
    edituser.resizable(False, False)
    edituser.configure(bg='black')
    edituser.title('Edit Employee')


    ######################## FRAME 1 ############################
    frame1 = Frame(edituser,height=screen_height *0.25, width= screen_width, bg= '#3b1c47')
    frame1.pack(side=TOP,  fill = BOTH, expand= YES)

    usernamevar = StringVar()
    usernamevar.set(name)
    username = Entry(frame1, textvariable= usernamevar, fg = '#22eba3', bg = '#3b1c47', font=('Arial',12))
    username.place(x=screen_width * 0.45, y=screen_height * 0.07)

    def back_func():
        # import employee_profile
        edituser.destroy()
        # employee_profile.elployeeprofile_func(id = 0,name=name, email=email, phone=phone, salary=salary, pic=pic, self='')

    back_icon = PhotoImage(file=r"assets/Back_PNG.png")
    back_icon =back_icon.zoom(1)
    back_icon =back_icon.subsample(70)
    back_btn = Button(frame1 ,image=back_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47', command=back_func)
    back_btn.place(x=screen_width * 0.92, y=screen_height * 0.04)



    ######################## FRAME 2 ############################
    frame2 = Frame(edituser,height=screen_height *0.75, width= screen_width, bg= 'black')
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
    useremailvar.set(email)
    useremail = Entry(frame2, textvariable=useremailvar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    useremail.place(x=screen_width * 0.45, y=screen_height * 0.05)

    phone_icon_path = PhotoImage(file='assets/Phone_PNG.png')
    phone_icon_path = phone_icon_path.zoom(1)
    phone_icon_path = phone_icon_path.subsample(55)
    phone_icon = Label(frame2, image= phone_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    phone_icon.place(x=screen_width * 0.35, y=screen_height * 0.21)

    userphonevar = StringVar()
    userphonevar.set(phone)
    userphone = Entry(frame2, textvariable=userphonevar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    userphone.place(x=screen_width * 0.45, y=screen_height * 0.21)

    salary_icon_path = PhotoImage(file='assets/Salary_PNG.png')
    salary_icon_path = salary_icon_path.zoom(1)
    salary_icon_path = salary_icon_path.subsample(55)
    salary_icon = Label(frame2, image= salary_icon_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = 'black')
    salary_icon.place(x=screen_width * 0.35, y=screen_height * 0.36)

    usersalaryvar = StringVar()
    usersalaryvar.set(salary)
    usersalary = Entry(frame2, textvariable=usersalaryvar, fg = '#22eba3', bg = 'black', font=('Arial',14))
    usersalary.place(x=screen_width * 0.45, y=screen_height * 0.36)

    imgpath = ''
    global selectedimagepath

    def update_user():
        global selectedimagepath
        if selectedimagepath != '':
            print('encoding... ')
            with open(selectedimagepath, 'rb') as file:
                # Reads each character
                selectedimage = base64.b64encode(file.read())
                conn = sqlite3.connect('employees.db')
                conn.execute("UPDATE USERS SET NAME = ?,EMAIL = ?,PHONE = ?,SALARY = ?,IMAGE=? WHERE ID=?", (usernamevar.get(),useremailvar.get(),userphonevar.get(),usersalaryvar.get(), selectedimage, id))
                conn.commit()
                conn.close()
                selectedimagepath = ''
        else:
            print('saving... ')
            conn = sqlite3.connect('employees.db')
            conn.execute("UPDATE USERS SET NAME=?,EMAIL=?,PHONE=?,SALARY=? WHERE ID=?", (usernamevar.get(),useremailvar.get(),userphonevar.get(),usersalaryvar.get(), id))
            conn.commit()
            conn.close()


    def submit_func():
        if(len(usernamevar.get()) == 0 or len(useremailvar.get()) == 0 or len(userphonevar.get()) == 0 or len(usersalaryvar.get()) == 0):
            messagebox.showerror('Error', 'Please fill all fields')
        else:
            # print(imgpath)
            # update_user()
            
            try:
                update_user()
                # useremailvar.set('')
                # usernamevar.set('')
                # userphonevar.set('')
                # usersalaryvar.set('')
                # imgpath = PhotoImage(file='assets/dummy_icon.png')
                # imgpath = imgpath.zoom(1)
                # imgpath = imgpath.subsample(1)
                # profile_pic.config(image=imgpath)
                messagebox.showinfo('success', 'user edited successfully')
            except:
                messagebox.showerror('error', 'unable to save data')
    submit_btn = Button(frame2, text='Submit', bg='#3b1c47',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',15),padx=15, command=submit_func)
    submit_btn.place(x=screen_width * 0.55, y=screen_height * 0.6)

    # imgpath = PhotoImage(data=pic)
    # imgpath = imgpath.zoom(1)
    # imgpath = imgpath.subsample(1)
    profile_pic = Label(edituser, image= pic, width= screen_height * 0.4 , height= screen_height * 0.55, bg = '#3b1c47')
    profile_pic.place(x=screen_width * 0.03, y=screen_height * 0.05)  


    def img_func():
        global imgpath, selectedimagepath
        imgpath = filedialog.askopenfilename(filetypes=[("Image File",'.png')])
        print(imgpath)
        if imgpath != '':
            selectedimagepath = imgpath
        else:
            selectedimagepath = ''
        # print(imgpath)
        # print(str(imgpath).split('/')[5] + '/' + str(imgpath).split('/')[6])
        if not imgpath == '':
            profile_pic_path = PhotoImage(file=imgpath)
            profile_pic_path = profile_pic_path.zoom(1)
            profile_pic_path = profile_pic_path.subsample(1)
            imgpath=profile_pic_path
            profile_pic.config(image=imgpath)
            # select_btn['state'] = DISABLED
        else:
            # imgpath = PhotoImage(data=pic)
            # imgpath = imgpath.zoom(1)
            # imgpath = imgpath.subsample(1)
            profile_pic.config(image=pic)
            


    select_btn = Button(frame2, text='Select Image', bg='black',activebackground='#3b1c47', activeforeground='white', fg='white',font=('Arial',8), command=img_func)
    select_btn.place(x=screen_width * 0.8, y=screen_height * 0.5)



    edituser.mainloop()
    
# adduser_func()