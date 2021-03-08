# Author : Srujan
# calculates the age based on the date entered

from tkinter import *
import datetime

# run on clicking the button
def calcAge():
    bDay = int(birthDayEntry.get())
    bMonth = int(birthMonthEntry.get())
    bYear = int(birthYearEntry.get())

    bDate = datetime.date(bYear,bMonth,bDay)
    today = datetime.date.today()

    txt = Text(height = 3,width = 50)
    txt.grid(row = 6,column = 1)

    notBorn = False

    years = today.year - bDate.year 
    months = today.month - bDate.month
    days = today.day - bDate.day

    if days < 0:
        months -= 1
        days += 31
    if months < 0:
        years -= 1
        months += 12
    if years < 0:
        notBorn = True

    if notBorn:
        txt.insert(INSERT,"Sorry kid, you are not born yet!")
    else:
        txt.insert(INSERT,"You are {} years {} months {} days old today! Damn!".format(years,months,days))

# start
root = Tk()
root.geometry("500x400")
root.title("Age Calculator")

# Labels
birthYear = Label(root,text = "Year : ",font = "Helvetica 12 bold")
birthMonth = Label(root,text = "Month : ",font = "Helvetica 12 bold")
birthDay = Label(root,text = "Day : ",font = "Helvetica 12 bold")

# Entry places for above labels
birthYearEntry = Entry(root,width = 50)
birthMonthEntry = Entry(root,width = 50)
birthDayEntry = Entry(root,width = 50)

# Aligning with grid system
birthDay.grid(column = 0,row = 1)
birthDayEntry.grid(column = 1,row = 1)

birthMonth.grid(column = 0,row = 2)
birthMonthEntry.grid(column = 1,row = 2)

birthYear.grid(column = 0,row = 3)
birthYearEntry.grid(column = 1,row = 3)

# Action button
calcButton = Button(root,text = "Calculate",padx = 40,pady = 10,bg = "grey",font = "Helvetica 12",command = calcAge)
calcButton.grid(row = 4,column = 1)

# pic for the program
image = PhotoImage(file = "images/ageCalc.png")
tinyImg = image.subsample(2,2)

label = Label(root,image = tinyImg)
label.grid(row = 0,column = 1)

root.mainloop()
# end