import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
from PIL import Image, ImageTk




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
            vscrollbar = ttk.Scrollbar(self, orient=VERTICAL, )
            vscrollbar.pack(fill=Y, side=RIGHT, expand=TRUE)
            canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                            yscrollcommand=vscrollbar.set)
            canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
            vscrollbar.config(command=canvas.yview)

            # Reset the view
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)
            # Create a frame inside the canvas which will be scrolled with it.
            self.interior = interior = Frame(canvas,bg='black')
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

            self.search_icon = PhotoImage(file=r"assets/Search_PNG.png")
            self.search_icon =self.search_icon.zoom(1)
            self.search_icon =self.search_icon.subsample(70)
            self.search_btn = Button(self.frame1 ,image=self.search_icon ,relief='flat',width= screen_height * 0.05 , height= screen_height * 0.05, bg = '#3b1c47', activebackground='#3b1c47')
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
            
            self.frame = VerticalScrolledFrame(root, bg='black')
            self.frame.pack()
            # self.label = ttk.Label(self, text="Shrink the window to activate the scrollbar.")
            # self.label.pack()
            for i in self.usersdata:
                self.profilepic = PhotoImage(data=i[5])
                self.profilepic = self.profilepic.zoom(1)
                self.profilepic = self.profilepic.subsample(2)
                self.usersimages.append(self.profilepic)
            buttons = []
            # var = dict()
            r = 0
            c = 0
            if len(self.usersdata) == 0:
                Label(self.frame.interior, text='No Employee Available',bg='black', fg = 'white', font=('Arial',20)).pack(anchor = CENTER, pady=50)
            else:
                for i in range(len(self.usersdata)):
                    if c == 4:
                        c=0
                        r  += 1
                    # for j in range(4):
                    userprofile = Button(self.frame.interior,text=self.usersdata[i][1], compound='top',image= self.usersimages[i],relief='flat',width= screen_height * 0.25 , height= screen_height * 0.25, bg = 'black', activebackground='black', fg= 'white')
                    buttons.append(userprofile)
                    # buttons.append(ttk.Button(self.frame.interior,image=self.profilepic, text="Button " + str(i)))
                    buttons[-1].grid(row = r+1, column = c+1, padx=15, pady=10, ipady = 20)
                    c += 1
                

    app = SampleApp()
    app.mainloop()
    
employees_func()