import tkinter as tk
from tkinter import ttk
from CommonTools import *

def saveToFile():
    

def makeSettingsTab(parent):
    newFrame = tk.Frame(parent)
    curCol = 0
    curRow = 0
    newButton = tk.Button(
        newFrame,
        text="save as",
        command=saveToFile()
    )
    newButton.grid(column=curCol, row=curRow)

    return newFrame