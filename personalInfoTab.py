import tkinter as tk
from tkinter import ttk
from CommonTools import createLabelEntry

def makePersonalInformationtab(parent, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail):
    newFrame = tk.Frame(parent)
    curCol = 0
    currRow = 0
    newEntry, newlabel = createLabelEntry(parent, "First name: ", firstName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "Middle Initial: ", middleInitial)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "Last name: ", lastName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "LinkedIn: ", userLinkedin)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "Github: ", userGithub)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "Phone Number: ", userPhone)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = createLabelEntry(parent, "Email : ", userEmail)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0 
    currRow += 1
    return newFrame
