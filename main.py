__author__ = 'mkv-aql'

import sys
import tkinter
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import ButtonFunctions

import matplotlib

import encrypt

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
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#___________________________________________CLASS WINDOWS_________________________________
#Adding multiple pages into the program window

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