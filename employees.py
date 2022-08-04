import functools
import sqlite3
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import customtkinter as ctk
from login import login_func




screen_height = 350
screen_width = 500

def employees_func():

    class VerticalScrolledFrame(Frame):
        """A pure Tkinter scrollable frame that actually works!
        * Use the 'interior' attribute to place widgets inside the scrollable frame.
        * Construct and pack/place/grid normally.
        * This frame only allows vertical scrolling.
        """
        def __init__(self, parent, *args, **kw):
            Frame.__init__(self, parent, *args, **kw)

            # Create a canvas object and a vertical scrollbar for scrolling it.
            vscrollbar = Scrollbar(self, orient=VERTICAL)
            vscrollbar.pack(fill=Y, side=RIGHT, expand=True,anchor='sw')
            canvas = Canvas(self, bd=0, highlightthickness=0, bg='black',
                            yscrollcommand=vscrollbar.set)
            canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
            vscrollbar.config(command=canvas.yview)

            # Reset the view
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)
            # Create a frame inside the canvas which will be scrolled with it.
            self.interior = interior = Frame(canvas, bg='black')
            interior_id = canvas.create_window(0, 0, window=interior,
                                            anchor=NW)

            # Track changes to the canvas and frame width and sync them,
            # also updating the scrollbar.
            def _configure_interior(event):
                # Update the scrollbars to match the size of the inner frame.
                size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
                canvas.config(scrollregion="0 0 %s %s" % size)
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # Update the canvas's width to fit the inner frame.
                    canvas.config(width=interior.winfo_reqwidth())
            interior.bind('<Configure>', _configure_interior)

            def _configure_canvas(event):
                if interior.winfo_reqwidth() != canvas.winfo_width():
                    # Update the inner frame's width to fill the canvas.
                    canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            canvas.bind('<Configure>', _configure_canvas)


    # if __name__ == "__main__":
        
    class SampleApp(tk.Tk):
        
        def __init__(self, *args, **kwargs):
            root = tk.Tk.__init__(self, *args, **kwargs)
            
            # screen_height = 350
            # screen_width = 500
            # self.geometry(f'{screen_width}x{screen_height}')
            # self.resizable(False, True)
            self.config(bg='black')
            self.usersdata = []
            self.usersimages = []
            def queryallusers():
                conn = sqlite3.connect('employees.db')
                rows = conn.execute("SELECT * FROM USERS")
                
                for row in rows:
                    self.usersdata.append(row)
                conn.close()
            try:
                queryallusers()
            except:
                pass
            self.title('Employees')
            self.configure(bg='black')
            ####################### FRAME 1 ############################
            self.frame1 = Frame(root,height=screen_height *0.15, width= screen_width, bg= '#3b1c47')
            self.frame1.pack(side=TOP,  fill = BOTH, expand= YES)

            self.logo_path = PhotoImage(file='assets/BIG_Iress_Logo.png')
            self.logo_path = self.logo_path.zoom(1)
            self.logo_path = self.logo_path.subsample(32)
            logo = Label(self.frame1, image= self.logo_path, width= screen_height * 0.1 , height= screen_height * 0.1, bg = '#3b1c47')
            logo.place(x=screen_width * 0.05, y=screen_height * 0.025)

            txt1 = Label(self.frame1, text='Employees', fg = '#22eba3', bg = '#3b1c47', font=('Arial',16))
            txt1.place(x=screen_width * 0.4, y=screen_height * 0.04)

            def execute_search(uname):
                print(uname)
                if uname == '':
                    pass
                else:
                    for button in self.buttons:    
                        if button['text'] != uname:
                            button.grid_forget()
                        # self.buttons.remove()
                #     self.usersimages = []
                #     self.usersdata = []
                #     # try:
                #     conn = sqlite3.connect('employees.db')
                #     rows = conn.execute(f"SELECT * FROM USERS WHERE name=?",(uname,))
                #     print(rows)
                #     for row in rows:
                #         self.usersdata.append(row)
                #     conn.close()
                #     print(len(self.usersdata))
                #     # print(self.usersdata)
                #     # self.usersimages = []
                #     # self.usersdata = []
                #     for i in self.usersdata:
                #         self.profilepic = PhotoImage(data=i[5])
                #         self.profilepic = self.profilepic.zoom(1)
                #         self.profilepic = self.profilepic.subsample(2)
                #         self.usersimages.append(self.profilepic)
                #     # except:
                #     #     messagebox.showerror('Error', 'Unable to search this user try again')
                #     # try:
                #     r = 0
                #     c = 0
                #     # self.frame.interior.grid_remove()                    
                #     # self.frame.pack_forget()
                #     self.buttons.clear()
                #     if len(self.usersdata) == 0:
                #         Label(self.frame.interior, text='No Employee Available', fg = 'white',bg='black', font=('Arial',30)).pack(anchor = CENTER, pady=100, padx=35)
                #     else:
                #         for i in range(len(self.usersdata)):
                #             print(c)
                #             if c == 4:
                #                 c=0
                #                 r  += 1
                #             # for j in range(4):
                #             self.userprofile = Button(self.frame.interior,text=self.usersdata[i][1], compound='top',image= self.usersimages[i],relief='flat',width= screen_height * 0.25 , height= screen_height * 0.25, bg = 'black', activebackground='black', fg= 'white')
                #             self.buttons.append(self.userprofile)
                #             self.buttons[1].text
                #             # buttons.append(ttk.Button(self.frame.interior,image=self.profilepic, text="Button " + str(i)))
                #             self.buttons[-1].grid(row = r+1, column = c+1, padx=15, pady=10, ipady = 20)
                #             self.userprofile.bind('<Button-1>', functools.partial(btn_func, name=self.usersdata[i][1], email=self.usersdata[i][2], phone=self.usersdata[i][3], salary=self.usersdata[i][4], pic=self.usersimages[i]))
                #             self.userprofile.bind('<Button-3>', functools.partial(do_popup, name=self.usersdata[i][1], email=self.usersdata[i][2], phone=self.usersdata[i][3], salary=self.usersdata[i][4], pic=self.usersimages[i]))
                #             c += 1
                # self.update_idletasks()
                    # except:
                        # messagebox.showerror('Error', 'Error occur while searching the user.')
                        

            def search_func():                
                execute_search(ctk.CTkInputDialog(self, title='Search User', text='Search By Username').get_input())
                    
            self.search_icon = PhotoImage(file=r"assets/Search_PNG.png")
            self.search_icon =self.search_icon.zoom(1)
            self.search_icon =self.search_icon.subsample(70)
            self.search_btn = Button(self.frame1 ,image=self.search_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47',command=search_func)
            self.search_btn.place(x=screen_width * 0.8, y=screen_height * 0.04)
            
            
            def add_func():
                import adduser
                self.destroy()
                adduser.adduser_func()

            self.add_icon = PhotoImage(file=r"assets/Add_PNG.png")
            self.add_icon =self.add_icon.zoom(1)
            self.add_icon =self.add_icon.subsample(70)
            self.add_btn = Button(self.frame1 ,image=self.add_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47', command= add_func)
            self.add_btn.place(x=screen_width * 0.9, y=screen_height * 0.04)
            
            self.frame = VerticalScrolledFrame(root, bg = 'black')
            self.frame.pack()
            # self.label = ttk.Label(self, text="Shrink the window to activate the scrollbar.")
            # self.label.pack()
            for i in self.usersdata:
                self.profilepic = PhotoImage(data=i[5])
                self.profilepic = self.profilepic.zoom(1)
                self.profilepic = self.profilepic.subsample(2)
                self.usersimages.append(self.profilepic)
            
            def do_popup(event, name, email, phone, salary, pic):
                self.m = Menu(root, tearoff = 0, bg='black', fg = 'white')
                # self.m.add_command(label ="Edit" ,background='black',foreground='white' ,command= functools.partial(edit_func, name, email, phone, salary, pic,))
                # self.m.add_separator()
                self.m.add_command(label ="Delete",background='black',foreground='white' , command= functools.partial(delete_profile, name=name, email=email,phone=phone,salary=salary,pic=pic))  
                try:
                    self.m.tk_popup(event.x_root, event.y_root)
                finally:
                    self.m.grab_release()
                
            def delete_profile(name, email, phone, salary, pic):
                global buttons, usersdata
                if(messagebox.askyesno('Are you sure?', 'Do you want to delete this user?')):
                    login_func(name, email, phone, salary, pic, isedit=False)
                    
                
            def btn_func(event,name, email, phone, salary, pic):
                import employee_profile
                self.withdraw()
                print(pic)
                employee_profile.elployeeprofile_func(name=name, email=email, phone=phone, salary=salary, pic=pic, self=self)
                
            self.buttons = []
            # var = dict()
            def creating_profiles():
                global buttons
                r = 0
                c = 0
                if len(self.usersdata) == 0:
                    Label(self.frame.interior, text='No Employee Available', fg = 'white',bg='black', font=('Arial',30)).pack(anchor = CENTER, pady=100, padx=35)
                else:
                    for i in range(len(self.usersdata)):
                        if c == 4:
                            c=0
                            r  += 1
                        # for j in range(4):
                        self.userprofile = Button(self.frame.interior,text=self.usersdata[i][1], compound='top',image= self.usersimages[i],relief='flat',width= screen_height * 0.25 , height= screen_height * 0.25, bg = 'black', activebackground='black', fg= 'white')
                        self.buttons.append(self.userprofile)
                        
                        # buttons.append(ttk.Button(self.frame.interior,image=self.profilepic, text="Button " + str(i)))
                        self.buttons[-1].grid(row = r+1, column = c+1, padx=15, pady=10, ipady = 20)
                        self.userprofile.bind('<Button-1>', functools.partial(btn_func, name=self.usersdata[i][1], email=self.usersdata[i][2], phone=self.usersdata[i][3], salary=self.usersdata[i][4], pic=self.usersimages[i]))
                        self.userprofile.bind('<Button-3>', functools.partial(do_popup, name=self.usersdata[i][1], email=self.usersdata[i][2], phone=self.usersdata[i][3], salary=self.usersdata[i][4], pic=self.usersimages[i]))
                        c += 1
            creating_profiles()
                

    app = SampleApp()
    app.mainloop()
    
# employees_func()