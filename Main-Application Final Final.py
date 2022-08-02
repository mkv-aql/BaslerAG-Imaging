#[NOTE TO SELF]
#Built-in console in the window, showing the program command
#Icon.ico will not work in raspbian, must be commented out
#cv2 will not work in raspbian, musst be commented out

#________________________________IMPORTING MODULES__________________________

#[IMPORTING SHITS]
    #[IMPORTING TKINTER]
import tkinter as tk
from tkinter import ttk
from tkinter import *

    #[IMPORTING MATPLOTLIB]
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

    #[IMPORTING CV2 FOR IMAGE PROCESSING]
#import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

    #[IMPORTING TURTLE]
from turtle import *
import turtle 

#__________________________________SET UP PHASE___________________________

#[ZUMO ROBOT PARAMETERS]
# Distance between x sensors
Xsensor = int(11.5)
# Distance between y sensors
Ysensor = int(6.5)
# Starting Coordinate of zumo robot
XX=0
YY=0
int(XX)
int(YY)
ZumoCoordinate = [XX,YY]

#[STYLE OF WINDOW]
style.use("ggplot")
LARGE_FONT = ("Verdana", 12)

#________________________________LIVE MAP UPDATE__________________________

#[CANVAS FOR GRAPH]
f = Figure(figsize = (7,7), dpi=100)
a = f.add_subplot(111)

#[DEFINING ANIMATION]
def animate(i):
    pullData = open("Dataplot.txt","r").read()
    dataList = pullData.split('\n')
    

    CountList = []
    wList = []
    xList = []
    yList = []
    zList = []

    # and or for && ||
    for eachLine in dataList:
        if len(eachLine) > 1 and len(dataList) > 1 :
            Count, w, x, y, z = eachLine.split(',')
            CountList.append(int(Count))
            wList.append(int(w))
            xList.append(int(x))
            yList.append(int(y))
            zList.append(int(z))


            #Send data to first coordinate1() for first reference of coordinate
            coordinate1(Count, w, x, y, z)

                
    #Clearing graph if needed 
    a.clear()
    #plotting x,y
    Line1, = a.plot(CountList, wList)
    Line2, = a.plot(CountList, xList)
    Line3, = a.plot(CountList, yList)
    Line4, = a.plot(CountList, zList)
    Legend1 = a.legend([Line1,Line2,Line3,Line4], ['Front','Left','Right','Back'])

def coordinate1(Count, w, x, y, z):
    
    #Front, Left, Right, Back
    FirstCoordinate = [Count, w, x, y, z]
    #print(FirstCoordinate) / Length of whole X / Y axis respective to zumo
    LengthOfX = int(w) + (Xsensor) + int(z)
    LengthOfY = int(x) + (Ysensor) + int(y)

    #print(LengthOfX, LengthOfY) # Prints the whole thing continously
    LeftWall = int(x) + ((Xsensor)/2)
    RightWall = int(y) + ((Xsensor)/2)
    FrontWall = int(w) + ((Ysensor)/2)
    BackWall = int(z) + ((Ysensor)/2)

    NextCount = int(Count) + 1
    Nextw = int(w)
    Nextx = int(x)
    Nexty = int(y)
    Nextz = int(z)
    
    

    return NextCount, Nextw, Nextx, Nexty, Nextz, LeftWall, RightWall, FrontWall, BackWall


#_______________________________WINDOW GUI__________________________________________

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, bitmap=None, default="Icon.ico")
        tk.Tk.wm_title(self, "Smart Bot Controller")
        
        #Containing the function
        container = tk.Frame(self)
        container.pack(side="top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #[Adding menu bar]
        menubar = tk.Menu(container)
        #not using tearoff
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="FUCK", command = lambda: popupmsg("Not Suppoirted yet"))
        filemenu.add_command(label="FUCK 2", command = lambda: popupmsg("Not Supported Yet"))
        filemenu.add_command(label="FUCK 3", command = lambda: popupmsg("Not Supported Yet"))
        #Adding seperator within dropdown
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu = filemenu)

        tk.Tk.configure(self, menu=menubar)

        #Create empty dictionary
        self.frames = {}

        #For Launching the "Page 1/2/3/4/5/6/7"
        for F in (StartPage, PageOne, PageTwo, PageThree,
                  PageFour, PageSeven):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#_______________________________DEFINING BUTTON FUNCTIONS____________________________________

#Condition Zero / Resest every data
def ConditionZero1():
    print("Clear Command list")
    i=0
    CMD = open("Command.txt", "w")
    #Delete text in .txt
    CMD.truncate(0)
    GoForward.counter = 0
    GoBackwards.counter = 0
    GoLeft.counter = 0
    GoRight.counter = 0

def ConditionZero2():
    print("Clear Map Coordinate list")
    i=0
    CMD = open("Dataplot.txt", "w")
    CMD.truncate(0)
    XCoordinate = 0
    YCoordinate = 0
    
#[ZUMO ROBOT MANUAL CONTROL]
#Defining function for buttons, and print to console
def Comment1(Entry11):
    data11 = Entry11
    print("Going Forward")
    GoForward(data11)

def Comment2(Entry12):
    data12 = Entry12
    print("Going Backwards")
    GoBackwards(data12)

def Comment3(Entry13):
    data13 = Entry13
    print("Going Left")
    GoLeft(data13)

def Comment4(Entry14):
    data14 = Entry14
    print("Going Right")
    GoRight(data14)

def qf2(param):
    print(param)

#Commands of the button: Create/write/erase Command.txt file
CurrentCount = 0
Count = CurrentCount
def GoForward(data11):
    d11 = data11
    CMD = open("Command.txt", "a+")
    GoForward.counter += 1
    CurrentCount = Count + GoForward.counter
    GoForward.counter = CurrentCount
    i = CurrentCount
    CMD.write("%i F %s\n" %(i, d11))
GoForward.counter = CurrentCount

def GoBackwards(data12):
    d12 = data12
    CMD = open("Command.txt", "a+")
    GoBackwards.counter += 1
    CurrentCount = Count + GoBackwards.counter
    GoBackwards.counter = CurrentCount
    i = CurrentCount
    CMD.write("%i B %s\n" %(i, d12))
GoBackwards.counter = CurrentCount

def GoLeft(data13):
    d13 = data13
    CMD = open("Command.txt", "a+")
    GoLeft.counter += 1
    CurrentCount = Count + GoLeft.counter
    GoLeft.counter = CurrentCount
    i = CurrentCount
    CMD.write("%i L %s\n" %(i, d13))
GoLeft.counter = CurrentCount

def GoRight(data14):
    d14 = data14
    CMD = open("Command.txt", "a+")
    GoRight.counter += 1
    CurrentCount = Count + GoRight.counter
    GoRight.counter = CurrentCount
    i = CurrentCount
    CMD.write("%i R %s\n" %(i, d14))
GoRight.counter = CurrentCount
#Calculations / Counter /

CurrentCount = CurrentCount + (GoForward.counter)
CurrentCount = CurrentCount + (GoBackwards.counter)
CurrentCount = CurrentCount + (GoLeft.counter)
CurrentCount = CurrentCount + (GoRight.counter)


#[ZUMO ROBOT AUTO CONTROL]
#Defining button of page 2 
#Command of the button in page 2
def AutoControl():
    CMD = open("Command.txt", "a+")
    AutoControl.counter += 1
    CurrentCount = Count + AutoControl.counter
    AutoControl.counter = CurrentCount
    i = CurrentCount
    CMD.write("AUTOCONTROL %i \n" %(i))
    print("Start Auto Control")
AutoControl.counter = CurrentCount


#___________________________________________CLASS WINDOWS_________________________________

#Adding multiple pages into the program window
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page Home", font = LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        button1 = ttk.Button(self, text = "Zumo Robot Manual Control",
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text = "Zumo Robot Auto Control",
                            command = lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text = "Go to page 3",
                            command = lambda: controller.show_frame(PageThree))
        button3.pack()

        button4=ttk.Button(self,text="Delete everything",
                          command=lambda: controller.show_frame(PageFour))
        button4.pack()

        button7 = ttk.Button(self, text = "Show 2nd Map",
                             command = lambda: [controller.show_frame(PageSeven), animate(0)])
        button7.pack()

        

#Making "Page 1" / "ZUMO ROBOT MANUAL CONTROL" 
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start PAge 1", font = LARGE_FONT)

        label.pack(pady=5,padx=5)

        #Go Forward Button
        EntryLabel11 = tk.Label(self, text = "cm")
        e1 = tk.Entry(self)
        data11 = e1.get()
        button11 = ttk.Button(self, text = "Go Forward",
                              command = lambda: [Comment1(e1.get()), e1.get(), print("%s cm" %(e1.get()))])
        button11.pack()
        EntryLabel11.pack()
        e1.pack(pady=5,padx=5)

        #Go Backwards Button
        EntryLabel12 = tk.Label(self, text = "cm")
        e2 = tk.Entry(self)
        data12 = e1.get()
        button12 = ttk.Button(self, text = "Go Backwards",
                              command = lambda: [Comment2(e2.get()), e2.get(), print("%s cm" %(e2.get()))])
        button12.pack()
        EntryLabel12.pack()
        e2.pack(pady=5,padx=5)
        
        #Go Left Button
        button13 = ttk.Button(self, text = "Go Left",
                              command = lambda: [Comment3(e3.get()), e3.get(), print("%s degrees" %(e3.get()))])
        button13.pack()
        EntryLabel13 = tk.Label(self, text = "degree")
        EntryLabel13.pack()
        e3 = tk.Entry(self)
        e3.pack(pady=5,padx=5)

        #Go Right Button 
        button14 = ttk.Button(self, text = "Go Right",
                              command = lambda: [Comment4(e4.get()), e4.get(), print("%s degrees" %(e4.get()))])
        button14.pack()
        EntryLabel14 = tk.Label(self, text = "degree")
        EntryLabel14.pack()
        e4 = tk.Entry(self)
        e4.pack(pady=5,padx=5)
        
        #Go to home button 
        button15 = ttk.Button(self, text = "Go to page Home",
                            command = lambda: controller.show_frame(StartPage))
        button15.pack()
        


#Making "Page 2" / "ZUMO ROBOT AUTO CONTROL" 
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page 2", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button21 = ttk.Button(self, text = "Button 2 test",
                            command = lambda: qf2("Button 2 Comment to console"))
        button21.pack()

        button22 = ttk.Button(self, text = "AUTO CONTROL", command = lambda: AutoControl())
        button22.pack() 

        button23 = ttk.Button(self, text = "Go to page Home",
                            command = lambda: controller.show_frame(StartPage))
        button23.pack()

#Making "Page 3"
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Start Page 3", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button31 = ttk.Button(self, text = "Go to page Home",
                            command = lambda: controller.show_frame(StartPage))
        button31.pack()

#Making "Page 4" / "Delete Everything" 
class PageFour(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Start Page 4 / Delete Everything PAge",font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button41 = ttk.Button(self, text = "Delete Command list NOW!",
                            command = lambda: ConditionZero1())
        button41.pack()

        button42 = ttk.Button(self, text = "Delete Coordinates / Clear Map NOW!",
                              command = lambda: ConditionZero2())
        button42.pack()

        button43 = ttk.Button(self,text="Go to Page Home",
                          command=lambda: controller.show_frame(StartPage))
        button43.pack()



#Making "Page 7", 2nd Live Graph
class PageSeven(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Start Page 7, 2nd Live Graph Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button71 = ttk.Button(self, text = "Go to Home Page",
                              command = lambda: controller.show_frame(StartPage))
        button71.pack()

        button72 = ttk.Button(self, text = "Print MazE map",
                              command = lambda: MazeDraw())
        button72.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        #Maze plotting / Turtle
        def MazeDraw():

            # Dataplot.txt fetching
            pullData = open("Dataplot3.txt","r").read()
            dataList = pullData.split('\n')
            

            CountList = []
            wList = []
            xList = []
            yList = []
            zList = []

            #Front, Left, Right Back
            for eachLine in dataList:
                if len(eachLine) > 1 and len(dataList) > 1 :
                    Count, w, x, y, z = eachLine.split(',')
                    CountList.append(int(Count))
                    wList.append(int(w))
                    xList.append(int(x))
                    yList.append(int(y))
                    zList.append(int(z))

                    coordinate1(Count, w, x, y, z)

            # 0 for first row
            Ref1 = int(0)
            Ref2 = int(1)
            print(wList[Ref1],xList[Ref1],yList[Ref1],zList[Ref1])
            #Ref2 = Ref1 + 1
            print(wList[Ref2],xList[Ref2],yList[Ref2],zList[Ref2])
            #Ref3 = Ref2 + 1
            #print(wList[Ref3],xList[Ref3],yList[Ref3],zList[Ref3])
            #Ref4 = Ref3 + 1
            print(wList, "\n")
            print(xList, "\n")
            print(yList, "\n")
            print(zList, "\n")
            

            #Turtle print
            turtle.setup(600,600)
            turtle1 = Turtle()
            turtle1.speed(2)
            turtle1.pencolor("blue")
            turtle1.left(90)
            #Move
            while True:
                if (wList[Ref1] != wList[Ref2] or zList[Ref1] != zList[Ref2]):
                    if (xList[Ref1] and yList[Ref1]) < 10 or (wList[Ref1]) > 10:
                        turtle1.forward(abs(int(wList[Ref2]) - int(wList[Ref1]))) #abs for number difference
                        Ref1 = Ref1 + 1
                        #Ref2 = Ref2 + 1

                    if ((xList[Ref1] > yList[Ref1]) and (wList[Ref1]) < 10):
                        turtle1.right(90)
                        Ref1 = Ref1 + 1
                        #Ref2 = Ref2 + 1
                        
                    if ((yList[Ref1] > xList[Ref1]) and (wList[Ref1]) < 10):
                        turtle1.left(90)
                        Ref1 = Ref1 + 1
                        #Ref2 = Ref2 + 1

                elif (CountList[Ref1]):
                    turtle1.home()
                    
                
            #turtle1.right(90)
            #turtle1.forward(wList[Ref1])
            #turtle1.forward(wList[Ref2])
            
            return None 
        


#_____________________________CALLING ALL OF THE PROGRAM___________________________    
        
#Calling into reality with live graph
app = SeaofBTCapp()
#Animating the graph function with 1000ms update rate
ani = animation.FuncAnimation(f, animate, interval=1000)
#Creating the size of the application
app.geometry("1080x600")
app.mainloop()
