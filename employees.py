from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ctk
import awesometkinter as atk

screen_height = 350
screen_width = 500

employees = Tk()
employees.geometry('500x350')
employees.resizable(False, False)
# employees.configure(bg=atk.DEFAULT_COLOR)
employees.title('Employees')
# s = ttk.Style()
# s.theme_use('default')

######################## FRAME 1 ############################
frame1 = Frame(employees,height=screen_height *0.1, width= screen_width, bg= '#3b1c47')
frame1.pack(side=TOP,  fill = BOTH, expand= YES)

logo_path = PhotoImage(file='assets/BIG_Iress_Logo.png')
logo_path = logo_path.zoom(1)
logo_path = logo_path.subsample(32)
logo = Label(frame1, image= logo_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = '#3b1c47')
logo.place(x=screen_width * 0.05, y=screen_height * 0.025)

txt1 = Label(frame1, text='Employees', fg = '#22eba3', bg = '#3b1c47', font=('Arial',16))
txt1.place(x=screen_width * 0.4, y=screen_height * 0.04)

search_icon = PhotoImage(file=r"assets/Search_PNG.png")
search_icon =search_icon.zoom(1)
search_icon =search_icon.subsample(70)
search_btn = Button(frame1 ,image=search_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47')
search_btn.place(x=screen_width * 0.8, y=screen_height * 0.04)



add_icon = PhotoImage(file=r"assets/Add_PNG.png")
add_icon =add_icon.zoom(1)
add_icon =add_icon.subsample(70)
add_btn = Button(frame1 ,image=add_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47')
add_btn.place(x=screen_width * 0.9, y=screen_height * 0.04)


######################## FRAME 2 ############################
frame2 = Frame(employees, bg= 'black')
frame2.pack(side=BOTTOM, fill = BOTH, expand= YES,)


# canvas = ctk.CTkScrollbar(frame2, orientation=VERTICAL)

# scroll = atk.Simpl(parent=frame2,orient=VERTICAL )
# canvas = atk.ScrollableFrame(parent=frame2, bg= 'black')


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas = Canvas(frame2, bg= 'black',scrollregion=(0,0,screen_height,screen_height))

scroll = Scrollbar(frame2,orient=VERTICAL)
scroll.config(command=canvas.yview)
canvas.config(height=screen_height *0.85, width= screen_width)
# canvas.config( yscrollcommand=scroll.set)
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# scroll.bind("<Configure>",myfunction)
profilepic = PhotoImage(file='assets/Sample_Employee_2.png')
profilepic = profilepic.zoom(1)
profilepic = profilepic.subsample(2)
# canvas.create_window((0,0),window=frame2,anchor='nw',)
def add_user(imgpath, xplace, yplace, username):
    userframe = Frame(canvas, bd=1, relief="flat", bg='#3b1c47',
                    width=screen_height * 0.3, height=screen_height * 0.3)   
    userframe.place(x=xplace, y=yplace)
    userprofile = Button(userframe ,image=profilepic,text=username,compound='bottom' ,relief='flat',width= screen_height * 0.25 , height= screen_height * 0.25, bg = 'black', activebackground='black')
    userprofile.pack(side=TOP)
    usersname = Label(userframe , text=username, fg = '#22eba3', bg = '#3b1c47', font=('Arial',13))
    usersname.pack(side=BOTTOM, anchor='center', pady=5)
    
xplaceadd = 0
yplaceadd = 0
for i in range(4):
    xplaceadd = 0
    for j in range(4):
        add_user(imgpath='assets/Search_PNG.png',username='shami', xplace= (screen_width * 0.03 + xplaceadd), yplace=(screen_height * 0.1 + yplaceadd))
        xplaceadd += screen_height * 0.33
    yplaceadd +=  screen_height * 0.43

scroll.pack(side=RIGHT, fill= Y, anchor='ne')
canvas.pack(side=LEFT,expand=True,fill=BOTH)
# canvas.pack(side=RIGHT, fill = BOTH, expand= YES,)

employees.mainloop()