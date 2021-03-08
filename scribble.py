# Author : Srujan
# simple text editor for reading files and writing new files

from os import fdopen
from tkinter import *
from tkinter import filedialog

# global variable to keep track of current file opened
current = "nofile"

# for creating new file
def newFileFunc():
    myText.delete(1.0,END)
    blankSpace = " "
    root.title(140*blankSpace+"New File")

# for reading the file chosen by the user
def readFileFunc():
    global current 
    myText.delete(1.0,END)

    textFile = filedialog.askopenfilename(initialdir="/My Documnets",title="Open file",filetypes=(("Text files","*.txt"),("Python files","*.py"),("All files","*.*")))
    fname = textFile

    blankSpace = " "
    root.title(120*blankSpace + f"{fname} is open to read")

    fp = open(fname,'r')
    contents = fp.read()
    myText.insert(END,contents)
    current = fname
    print(current)
    fp.close()

# for saving the file written by the user as something
def saveAsFunc():
    textFile = filedialog.asksaveasfilename(defaultextension=".*",initialdir="/My Documents",title="Save File as",filetypes=(("Text files","*.txt"),("Python files","*.py"),("All files","*.*")))
    
    if textFile:
        fname = textFile

        global current
        current = fname
        
        contents = myText.get(1.0,END)
        fp = open(fname,'w+')
        fp.write(contents)

        blankSpace = " "
        root.title(130*blankSpace + "Saved as" + current)

        fp.close()

# for saving changes to an opened file
def saveFunc():
    global current

    if current == "nofile":
        saveAsFunc()
    else:
        fp = open(current,'w+')
        print(current)

        blankSpace = " "
        root.title(120*blankSpace + "Saving file " + current)

        fp.write(myText(1.0,END))
        fp.close()

# for info side box
def getInfo():
    top = Toplevel(root)
    top.title("Welcome to Help")
    info = Label(top,text="It gives info on the editor.")
    info.pack()
    b = Button(top,text="Dismiss",command=top.destroy)
    b.pack()

# start
root = Tk()
blankSpace = " "
root.title(130*blankSpace+"Scribble - text editor")

menuBar = Menu(root)
root.config(menu=menuBar)

textFrame = Frame(root)
textFrame.pack(pady=4)

textScroll = Scrollbar(textFrame)
textScroll.pack(side=RIGHT,fill=Y)

myText = Text(textFrame,height=20,width=100,font=("Helvetica",14),selectbackground="light green",selectforeground="brown",undo=True,yscrollcommand=textScroll.set)
myText.pack()

fileMenu = Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="File",menu=fileMenu)

newFileImg = PhotoImage(file="images/newfile.png")
newFileImg = newFileImg.subsample(8,8)
fileMenu.add_command(label="New file",image=newFileImg,compound=LEFT,command=newFileFunc)

readFileImg = PhotoImage(file="images/readfile.png")
readFileImg = readFileImg.subsample(9,9)
fileMenu.add_command(label="Read file",image=readFileImg,compound=LEFT,command=readFileFunc)

saveImg = PhotoImage(file="images/save.png")
saveImg = saveImg.subsample(8,8)
fileMenu.add_command(label="Save",image=saveImg,compound=LEFT,command=saveFunc)

saveAsImg = PhotoImage(file="images/saveas.png")
saveAsImg = saveAsImg.subsample(9,9)
fileMenu.add_command(label="Save As",image=saveAsImg,compound=LEFT,command=saveAsFunc)

fileMenu.add_separator()

quitImg = PhotoImage(file="images/quit.png")
quitImg = quitImg.subsample(7,7)
fileMenu.add_command(label="Quit",image=quitImg,compound=LEFT,command=root.destroy)

editMenu = Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Edit",menu=editMenu)

undoImg = PhotoImage(file="images/undo.png")
undoImg = undoImg.subsample(9,9)
editMenu.add_command(label="Undo",image=undoImg,compound=LEFT,command=myText.edit_undo)

redoImg = PhotoImage(file="images/redo.png")
redoImg = redoImg.subsample(9,9)
editMenu.add_command(label="Redo",image=redoImg,compound=LEFT,command=myText.edit_redo)

pasteImg = PhotoImage(file="images/paste.png")
pasteImg = pasteImg.subsample(7,7)
editMenu.add_command(label="Paste",image=pasteImg,compound=LEFT)

copyImg = PhotoImage(file="images/copy.png")
copyImg = copyImg.subsample(4,4)
editMenu.add_command(label="Copy",image=copyImg,compound=LEFT)

cutImg = PhotoImage(file="images/cut.png")
cutImg = cutImg.subsample(9,9)
editMenu.add_command(label="Cut",image=cutImg,compound=LEFT)

helpMenu = Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Info",command=getInfo)

root.mainloop()
# end