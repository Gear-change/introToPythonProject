import tkinter as tk
from tkinter import ttk
from commontools2 import create_label_entry

def makePersonalInformationtab(parent, firstName, middleInitial, lastName, userLinkedin, 
                               userGithub, userPhone, userEmail):
    newFrame = tk.Frame(parent)
    curCol = 0
    currRow = 0
    newEntry, newlabel = create_label_entry(parent, "First name: ", firstName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "Middle Initial: ", middleInitial)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "Last name: ", lastName)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "LinkedIn: ", userLinkedin)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "Github: ", userGithub)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "Phone Number: ", userPhone)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0
    currRow += 1
    newEntry, newlabel = create_label_entry(parent, "Email : ", userEmail)
    newlabel.grid(column=curCol,row=currRow)
    curCol += 1
    newEntry.grid(column=curCol,row=currRow)
    curCol = 0 
    currRow += 1
    return newFrame
