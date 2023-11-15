import tkinter as tk
from tkinter import ttk

def createComboSet(parent, labelText, input, listOfValues):
    newComboBox = ttk.Combobox(parent, textvariable=input, values=listOfValues)
    newLabel = tk.Label(parent, text=labelText)
    return newComboBox, newLabel

def createLabelEntry(parent, labelText, input):
    thislabel = ttk.Label(parent, text=labelText)
    entry = tk.Entry(parent, textvariable=input )
    return entry, thislabel

def createCheckBoxLabel(parent, stringText, input):
    thisCheckBox = ttk.Checkbutton(parent, text=stringText, variable=input, 
                                   offvalue=False, onvalue=True)
    return thisCheckBox

def createLabelTextField(parent, labelText, input):
    
    label = ttk.Label(parent, text=labelText, wraplength=125)
    input = tk.Text(parent, width=50, height=6)
    return label, input

def createSpinMonthYear(parent, labelText, month, year, yearsList):
    newLabel = ttk.Label(parent, text=labelText)
    newComboBox = ttk.Combobox(parent, width = 5,
                               textvariable = month,
                               values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newLabel2 = ttk.Label(parent, text=" - ")
    newComboBox1 = ttk.Combobox(parent, width = 5,
                               textvariable = year,
                               values = yearsList)
    month.set(1)
    year.set(1950)
    return newLabel, newComboBox, newLabel2, newComboBox1

def makeListFromText(textBoxIn, StringDetailName):
    tempString = textBoxIn.get("1.0", 'end-1c')
    listout = []
    listTempIn = tempString.split('\n')
    for item in listTempIn:
        if len(item) !=0:
            newDictDetail = {
                StringDetailName:item,
                "isRelevent":True
                }
            listout.append(newDictDetail)
    return(listout)