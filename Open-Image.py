import tkinter
from tkinter import *
from PIL import Image, ImageTk
import hashlib


root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("cat.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
root.geometry("1080x600")
root.mainloop()