__author__ = 'mkv-aql'

import sys
import tkinter
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import ButtonFunctions

import matplotlib

#Personal file imports
import encrypt
from Userlist import UserInput, UserDict

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

LARGE_FONT = ("Verdana", 12)


class BaslerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, bitmap=None, default="Icon.ico")
        tk.Tk.wm_title(self, "Image processing application")

        # Containing the function
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # [Adding menu bar]
        menubar = tk.Menu(container)
        # not using tearoff
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="dliawhuiawhda", command=lambda: popupmsg("Not Suppoirted yet"))
        filemenu.add_command(label="test test test", command=lambda: popupmsg("Not Supported Yet"))
        filemenu.add_command(label="FUCK YOU", command=lambda: popupmsg("Not Supported Yet"))
        # Adding seperator within dropdown
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.configure(self, menu=menubar)

        # Create empty dictionary
        self.frames = {}

        # For Launching the "Page 1/2/3/4/5/6/7"
        for F in (LoginPage, StartPage, PageOne, CreateAccount):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        ##Starting page when first run
        #self.show_frame(StartPage)
        self.show_frame(LoginPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#___________________________________________CLASS WINDOWS_________________________________
#Adding multiple pages into the program window

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Login PAge", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # Login entry space with button
        EntryLabel11 = tk.Label(self, text="User Name")
        e1 = tk.Entry(self)
        EntryLabel12 = tk.Label(self, text="Password")
        e2 = tk.Entry(self)
        button11 = ttk.Button(self, text="Login",
                              command=lambda: [e1.get(), e2.get(), print("Inserted user name: %s, Password: %s <<<<" % (e1.get(), e2.get()))])
        EntryLabel11.pack()
        e1.pack(pady=5, padx=5)
        EntryLabel12.pack()
        e2.pack(pady=5, padx=5)

        button11.pack()

        button12 = ttk.Button(self, text="Create new account",
                             command=lambda: controller.show_frame(CreateAccount))

        button12.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Main MEnu", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text= "Encrypt an image",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Watermarking an image",
                             command=lambda: print("Do Something here!"))
        button2.pack()


# Making "Page 1"
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Encrypt an Image", font=LARGE_FONT)

        label.pack(pady=5, padx=5)

        # Encrypt an image button, by running encrypt.py
        button11 = ttk.Button(self, text="Encrypt selected image",
                              command=lambda: ButtonFunctions.imageEncrypt())
        button11.pack()

class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Create new account", font=LARGE_FONT)

        label.pack(pady=5, padx=5)

        #Entry for new accounts (username and password)
        EntryLabel11 = tk.Label(self, text="User Name")
        e1 = tk.Entry(self)
        EntryLabel12 = tk.Label(self, text="Password")
        e2 = tk.Entry(self)

        EntryLabel11.pack()
        e1.pack(pady=5, padx=5)
        EntryLabel12.pack()
        e2.pack(pady=5, padx=5)

        #Insert user input and password into UserlistExample.py dictionary
        button11 = ttk.Button(self, text="Create",
                              command=lambda: [UserInput.insertuser(e1.get(), e2.get()), print(UserDict.username)])
        button11.pack()


""" 
def button1():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    image1 = Image.open('cat.jpg')
    canvas.create_image(50, 10, image = image1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1

root = Tk()
button1 = Button(root,text ='Sklop',command = button1, height=5, width=20).pack()

root.mainloop()
"""

app = BaslerApp()
app.geometry("1080x600")
app.mainloop()