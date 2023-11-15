import tkinter as tk
from tkinter import ttk
from CommonTools import *
from tkinter.filedialog import asksaveasfile

def formatStringOut(List):
    stringOut = ""
    for item in List:
        stringOut = stringOut.join(item)
        stringOut = stringOut.join("\n-1\n")
    return stringOut

def saveToFile(
        firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, 
        userEmail, userWork, userEducation, userSkills, userProjects
        ):
    #first we prepare the values in a string so we can print them
    stringToSave = ""
    lstPI = [
        firstName.get(), middleInitial.get(), lastName.get(), 
        userLinkedin.get(), userGithub.get(), userPhone.get(),
        userEmail.get()]
    stringToAdd = formatStringOut(lstPI)
    stringToSave = stringToSave.join(stringToAdd)
    #PI tab is done
    if len(userEducation) < 0:
        for dict in userEducation:
            stringToSave = stringToSave.join(str(dict))
            stringToSave = stringToSave.join("\n")
    stringToSave = stringToSave.join("\n-1\n")
    #education info done
    if len(userWork) < 0:
        for dict in userWork:
            stringToSave = stringToSave.join(str(dict))
            stringToSave = stringToSave.join("\n")
    stringToSave = stringToSave.join("\n-1\n")
    #work info read
    if len(userSkills) < 0:
        for dict in userSkills:
            stringToSave = stringToSave.join(str(dict))
            stringToSave = stringToSave.join("\n")
    stringToSave = stringToSave.join("\n-1\n")
    #skill info read
    if len(userProjects) < 0:
        for dict in userProjects:
            stringToSave = stringToSave.join(str(dict))
            stringToSave = stringToSave.join("\n")
    stringToSave = stringToSave.join("\n-1\n")
    files = [('All Files', "*.*"),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    file.write(stringToSave)
    file.close()

def makeSettingsTab(
        parent, firstName, middleInitial, lastName, userLinkedin, 
        userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects
        ):
    newFrame = tk.Frame(parent)
    curCol = 0
    curRow = 0
    newButton = tk.Button(
        newFrame,
        text="save as",
        command = lambda:saveToFile(
            firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, 
            userEmail, userWork, userEducation, userSkills, userProjects)
    )
    newButton.grid(column=curCol, row=curRow)

    return newFrame