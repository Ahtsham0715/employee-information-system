from tkinter import *



screen_height = 350
screen_width = 500

employees = Tk()
employees.geometry('500x350')
employees.resizable(False, False)
employees.configure(bg='black')
employees.title('Employees')
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
frame2 = Frame(employees,height=screen_height *0.8, width= screen_width, bg= 'black')
frame2.pack(side=BOTTOM, fill = BOTH, expand= YES)



employees.mainloop()