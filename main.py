import sys
import tkinter
from tkinter import *
from PIL import Image, ImageTk

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