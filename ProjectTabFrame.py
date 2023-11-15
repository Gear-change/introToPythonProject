from CommonTools import *
import tkinter as tk
from tkinter import ttk

def addNewProject(projectName, hasEvent, eventName, monthEvent, yearEvent, projectDetailsList):
    newProject = {
        "projectName":projectName,
        "hasEvent":hasEvent,
        "eventName":eventName,
        "month":monthEvent,
        "year":yearEvent,
        "isRelevent":True,
        "projectDetails":projectDetailsList,
    }
    global userProjects
    userProjects.append(newProject)

def makeOtherTab(parent):
    # ... Declare other StringVar or IntVar variables ...
    
    newFrame = tk.Frame(parent)
    projectName = tk.StringVar()
    hasEvent = tk.BooleanVar()
    eventName = tk.StringVar()
    monthEvent = tk.IntVar()
    yearEvent = tk.IntVar()
    projectDetailsText = tk.Text()
    yearsList = [year for year in range(1950, 2050)]

    #setting default for auto population
    
    projectName.set("Project")
    hasEvent.set(True)
    eventName.set("Event")
    monthEvent.set(1)
    yearEvent.set(1950)

    # ... Populate Education Tab with labels, entries, comboboxes ...
    currCol = 0
    currRow = 0
    newLabel = tk.Label(
        newFrame, 
        text="this Tab is for all other things which you may wish to put on your resume, whether they be projects, competitions, awards, or other such things.", 
        wraplength=300
        )
    newLabel.grid(column=currCol,row=currRow,columnspan=2)
    currRow += 1
    newEntry, newLabel = createLabelEntry(
        newFrame, 
        "Enter The name of this thing: ", 
        projectName
        )
    newLabel.grid(column=currCol,row=currRow)
    currCol += 1
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    newCheckBox = createCheckBoxLabel(newFrame, "This is a Compatition.", hasEvent)
    newCheckBox.grid(column=currCol,row=currRow, columnspan=2)
    currRow += 1
    newEntry, newLabel = createLabelEntry(newFrame, 
                                          "Enter the event's name: ", eventName)
    newLabel.grid(column=currCol,row=currRow)
    currCol += 1
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    newLabel, newComboBox, newLabel2, newComboBox2 = createSpinMonthYear(
        newFrame, 
        "Enter the month the thing took place:", 
        monthEvent, yearEvent, yearsList
        )
    newLabel2 = ttk.Label(newFrame, 
                          text="Enter the year that this thing took place in", 
                          wraplength=125)
    newLabel.grid(column=currCol,row=currRow)
    currCol += 1
    newComboBox.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    newLabel2.grid(column=currCol,row=currRow)
    currCol += 1
    newComboBox2.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    newLabel, projectDetailsText = createLabelTextField(
        newFrame, 
        "enter the details of this event: ", 
        projectDetailsText)
    newLabel.grid(column=currCol,row=currRow)
    currCol += 1
    projectDetailsText.grid(column=currCol,row=currRow)
    currRow += 1
    # Add Degree Button
    newButton = tk.Button(newFrame, text="Add Degree", 
                                command=lambda:addNewProject(
                                    projectName.get(),
                                    hasEvent.get(),
                                    eventName.get(),
                                    monthEvent.get(),
                                    yearEvent.get(),
                                    makeListFromText(
                                        projectDetailsText, 
                                        "projectDetail"
                                        )
                                    ))
    #return frame
    return newFrame