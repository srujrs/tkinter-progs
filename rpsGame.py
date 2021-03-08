# Author : Srujan
# Rock Paper Scissor game with computer

import random
from tkinter import *

userScore = 0
userChoice = ""
compScore = 0
compChoice = ""

dict = {'rock' : 0,'paper' : 1,'scissor' : 2}

def getNum(str):
    global dict
    return dict[str]

def result(user,comp):
    textArea.delete(0.0,END)

    userNum = getNum(user)
    compNum = getNum(comp)

    global userScore
    global compScore

    if userNum == compNum:
        textArea.insert(INSERT,"It's a Tie!\n")
    elif (userNum + 1)%3 == compNum:
        textArea.insert(INSERT,"Computer wins!\n")
        compScore += 1
    else:
        textArea.insert(INSERT,"You win!\n")
        userScore += 1

    ans = "\nYour choice : {uc} \nComputer's choice : {cc} \n\nYour score : {u} \nComputer's score : {c}".format(uc = user,cc = comp,u = userScore,c = compScore)
    textArea.insert(END,ans)

def randCompChoice():
    return random.choice(['rock','paper','scissor'])

def rock():
    global userChoice
    global compChoice
    userChoice = 'rock'
    compChoice = randCompChoice()
    result(userChoice,compChoice)

def paper():
    global userChoice
    global compChoice
    userChoice = 'paper'
    compChoice = randCompChoice()
    result(userChoice,compChoice)

def scissors():
    global userChoice
    global compChoice
    userChoice = 'scissor'
    compChoice = randCompChoice()
    result(userChoice,compChoice)

root = Tk()
root.title("Rock Paper Scissor Game")

button1 = Button(text = "   Rock        ",bg = "skyblue",font = "Helvetica 13 bold italic",command = rock)
button1.grid(column = 0,row = 1)
button2 = Button(text = "   Paper       ",bg = "lightgreen",font = "Helvetica 13 bold italic",command = paper)
button2.grid(column = 0,row = 2)
button3 = Button(text = "   Scissor    ",bg = "pink",font = "Helvetica 13 bold italic",command = scissors)
button3.grid(column = 0,row = 3)

textArea = Text(root,height = 12,width = 60,bg = "yellow")
textArea.insert(INSERT,"Let's play Rock-Paper-Scissor with the computer.\nCan you outsmart a computer?\nClick on the above buttons for your choice.\nLet's see what happens.")
textArea.grid(column = 0,row = 4)

root.mainloop()