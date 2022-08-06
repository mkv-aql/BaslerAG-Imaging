import sys
import tkinter
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

#[STYLE OF WINDOW]
style.use("ggplot")
LARGE_FONT = ("Verdana", 12)


class BaslerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, bitmap=None, default="Icon.ico")
        tk.Tk.wm_title(self, "Smart Bot Controller")

        # Containing the function
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # [Adding menu bar]
        menubar = tk.Menu(container)
        # not using tearoff
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="FUCK", command=lambda: popupmsg("Not Suppoirted yet"))
        filemenu.add_command(label="FUCK 2", command=lambda: popupmsg("Not Supported Yet"))
        filemenu.add_command(label="FUCK 3", command=lambda: popupmsg("Not Supported Yet"))
        # Adding seperator within dropdown
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.configure(self, menu=menubar)

        # Create empty dictionary
        self.frames = {}

        # For Launching the "Page 1/2/3/4/5/6/7"
        for F in (StartPage, PageOne, PageTwo, PageThree,
                  PageFour, PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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