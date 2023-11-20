import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox
import json

from relevencyFrame import openRelevencyFrame


def load_from_file(*args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    readFile = askopenfile(mode='r', filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")])
    if readFile is not None:
        #this if clause is in case there is no info in the file selected or no file there
        #first lets clear the existing files
        listStringFromFile = []
        for x in readFile:
            listStringFromFile.append(x)
        readFile.close()
        tempInt = 0
        listArgs =[]
        for x in listStringFromFile:
            listArgs.append(json.loads(x))
        listPIIN = listArgs[0]
        listPIset =[firstName ,middleInitial ,lastName ,userLinkedin ,userGithub ,userPhone ,userEmail ]
        for x in range(0,7):
            listPIset[x].set(listPIIN[x])
        userwork = listArgs[1]
        userEducation = listArgs[2]
        userskills = listArgs[3]
        userProjects = listArgs[4]
        
                 
    else:
        messagebox.showerror(title="there is nothing here", message="try a different file?")

def save_to_file(*args):
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    PIList = [firstName.get(),middleInitial.get(),lastName.get(),userLinkedin.get(),userGithub.get(),userPhone.get(),userEmail.get()]
    listArgs = []
    listArgs.append(PIList)
    listArgs.append(userWork)
    listArgs.append(userEducation)
    listArgs.append(userSkills)
    listArgs.append(userProjects)
    stringVarOut = ""
    for item in listArgs:
        tempString = stringVarOut + json.dumps(item) + "\n"
        stringVarOut = tempString
    
    string_to_save = stringVarOut
    print
    with asksaveasfile(filetypes=[('Text Document', '*.txt'), ('All Files', "*.*")], defaultextension='.txt') as file:
        if file:
            file.write(string_to_save)

def make_settings_tab(parent, *args):
    new_frame = tk.Frame(parent)
    curcol = 0
    curRow = 0
    new_label = tk.Label(new_frame, text="use the button here to save the current inputs to a file: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    save_button = tk.Button(new_frame, text="Save As", command=lambda: save_to_file(*args))
    save_button.grid(column=curcol,row=curRow)
    curRow += 1
    curcol = 0
    new_label = tk.Label(new_frame, text="use the button here to load prior inputs from a previous file: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    load_button = tk.Button(new_frame, text="open file", command=lambda: load_from_file(*args))
    load_button.grid(column=curcol,row=curRow)
    curRow += 1
    curcol = 0
    new_label = tk.Label(new_frame, text=" use this Button to proceed toward printing a resume: ")
    new_label.grid(column=curcol,row=curRow)
    curcol += 1
    to_relevency_button = tk.Button(new_frame, text="to relevancy input", command=lambda:openRelevencyFrame(*args))
    to_relevency_button.grid(column=curcol,row=curRow)
    return new_frame


