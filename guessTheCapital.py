# Author : Srujan
# guess the capital game

from os import write
from tkinter import *
from tkinter import simpledialog,messagebox

world = {}

def readFile():
    fp = open("countries.txt",'r')
    for line in fp:
        line = line.rstrip("\n")
        country,capital = line.split('-')
        world[country] = capital

    fp.close()

def writeFile(country,capital):
    fp = open("countries.txt",'a')
    fp.write("\n" + country + "-" + capital)

    fp.close()

root = Tk()
root.withdraw()

readFile()

while True:
    askCountry = simpledialog.askstring("Guess the capital","Enter the name of the country : ")
    
    if askCountry == None:
        break
    
    if askCountry == "":
        messagebox.showerror("Wrong","Country name can't be empty")
    else:
        capital = ""
        for i in world:
            if askCountry.lower() == i.lower():
                capital = world[i]
                break

        if capital != "":
            messagebox.showinfo("Capital","The capital city of " + askCountry + " is " + capital + "!")
        else:
            teach = simpledialog.askstring("Teach me","I don't know! What is the capital of" + askCountry + "?")
            if teach == "":
                messagebox.showerror("Wrong","Capital name can't be empty!")
            elif teach != None:
                world[askCountry.title()] = teach.title()
                writeFile(askCountry.title(),teach.title())

root.mainloop()