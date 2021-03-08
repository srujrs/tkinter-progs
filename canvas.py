# Author : Srujan
# Simple implementation of Paint with thickness meter, color chooser (using RGB values entered)
# and clear button to clear the screen

from tkinter import *
from tkinter import messagebox

# global variables inside functions
thickness = 1
previousX = 0
previousY = 0

# clears RGB values after accepted
def clearEntryfield():
    redVal.delete(0,END)
    greenVal.delete(0,END)
    blueVal.delete(0,END)
    leftFrame.focus()

# changes color based on the input given in RGB
def setLineColour():
    global colourRgb

    val1 = int(redVal.get())
    val2 = int(greenVal.get())
    val3 = int(blueVal.get())

    if (0 <= val1 <= 255) and (0 <= val2 <= 255) and (0 <= val3 <= 255):
        colourRgb = "#%02x%02x%02x" % (val1,val2,val3)
        chosenColour.config(bg=colourRgb)
        clearEntryfield()
    else:
        messagebox.showinfo("Error","Please enter a number between 0-255")
        clearEntryfield()

# changes thicknes based on the scale's value
def setThickness(event):
    global thickness
    thickness = thicknessScale.get()

# setting global vars to hold position of the last position of mouse 
# while drawing
def setPreviousXY(event):
    global previousX 
    global previousY 

    previousX = event.x
    previousY = event.y 

# draws lines when hovered with left click 
def drawLine(event):
    global previousX
    global previousY
    global colourRgb
    global thickness

    canv.create_line(previousX,previousY,event.x,event.y,width=thickness,fill=colourRgb)
    previousX = event.x 
    previousY = event.y

# clear the screen
def clearCanvas():
    canv.delete("all")

# start
root = Tk()

# variable to hold RGB value
colourRgb = "#%02x%02x%02x" % (128,192,200)

# frame to hold all entries, buttons and labels
leftFrame = Frame(root,bg=colourRgb)
leftFrame.pack(side=LEFT,fill=Y)

# colour label
colourLabel = Label(leftFrame,text="Choose a RGB colour",relief=RAISED,font=("Aerial",12,"bold"))
colourLabel.grid(row=0,column=0,sticky=NW,pady=4,padx=5)

# frame to hold colour entries
colourFrame = Frame(leftFrame)
colourFrame.grid(row=1,column=0,sticky=NW,pady=2,padx=3)

# RGB entries
redVal = Entry(colourFrame,width=7,insertwidth=3)
redVal.grid(row=0,column=0,pady=2,padx=4)
greenVal = Entry(colourFrame,width=7,insertwidth=3)
greenVal.grid(row=0,column=1,pady=2,padx=4)
blueVal = Entry(colourFrame,width=7,insertwidth=3)
blueVal.grid(row=0,column=2,pady=2,padx=4)

# colour display label
chosenColour = Label(colourFrame,bg="White",width=21)
chosenColour.grid(row=1,column=0,columnspan=3,pady=2,padx=4)

# button for choosing colour
acceptButton = Button(leftFrame,text="ACCEPT",command=setLineColour)
acceptButton.grid(row=2,column=0,sticky=NW,pady=2,padx=3)

# skip a row in the grid
leftFrame.grid_rowconfigure(3,minsize=50)

# thickness label
thicknessLabel = Label(leftFrame,text="Set line thickness:",font=("Aerial",12,"bold"))
thicknessLabel.grid(row=4,column=0,sticky=NW,pady=2,padx=3)

# thickness scale
thicknessScale = Scale(leftFrame,from_=1,to=20,orient=HORIZONTAL,command=setThickness)
thicknessScale.grid(row=5,column=0,sticky=S,pady=2,padx=3)

# skip a row in the grid
leftFrame.grid_rowconfigure(6,minsize=150)

# clear button
clearButton = Button(leftFrame,text="Clear",command=clearCanvas,relief=RAISED)
clearButton.grid(row=7,column=0,sticky=W+E,pady=2,padx=3)

# canvas to show what we have drawn
canv = Canvas(root,height=800,width=500,relief=RAISED,borderwidth=5)
canv.pack()

# event listeners for the canvas
canv.bind("<B1-Motion>",drawLine)
canv.bind("<Button-1>",setPreviousXY)

root.mainloop()
# end