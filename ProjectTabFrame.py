from tkinter import messagebox
from commontools2 import *
import tkinter as tk
from tkinter import ttk

def addNewProject(projectName, hasEvent, eventName, monthEvent, yearEvent, projectDetailsList):
    """
    Adds a new project to the user projects list.
    
    Args:
        projectName (str): Name of the project.
        hasEvent (bool): Whether the project has an event.
        eventName (str): Name of the event.
        monthEvent (int): Month of the event.
        yearEvent (int): Year of the event.
        projectDetailsList (list): List of details about the project.
    """
    newProject = {
        "projectName": projectName,
        "hasEvent": hasEvent,
        "eventName": eventName,
        "month": monthEvent,
        "year": yearEvent,
        "isRelevent": True,
        "projectDetails": projectDetailsList,
    }
    global userProjects
    userProjects.append(newProject)

def makeOtherTab(parent, listProjects):
    """
    Creates the project tab frame and populates it with input fields.
    
    Args:
        parent (tk.Widget): The parent widget for the tab frame.
        listProjects (list): The list of user's projects.
    
    Returns:
        tk.Frame: The created frame for the project tab.
    """
    global userProjects
    userProjects = listProjects
    
    # Create StringVar and IntVar variables for project details
    newFrame = tk.Frame(parent, name="otrFrame")
    projectName = tk.StringVar(parent, name="projectName")
    hasEvent = tk.BooleanVar(parent, name="hasEvent")
    eventName = tk.StringVar(parent, name="eventName")
    monthEvent = tk.IntVar(parent, name="monthEvent")
    yearEvent = tk.IntVar(parent, name="yearEvent")
    projectDetailsText = tk.Text(parent, name="projectDetailsText")
    yearsList = list(range(1950, 2050))

    # Setting default values
    projectName.set("Project")
    hasEvent.set(True)
    eventName.set("Event")
    monthEvent.set(1)
    yearEvent.set(1950)

    # Populate Project Tab with labels, entries, comboboxes
    currCol, currRow = 0, 0
    newLabel = tk.Label(newFrame, text="This tab is for all other things which you may wish to put on your resume, whether they be projects, competitions, awards, or other such things.", wraplength=300)
    newLabel.grid(column=currCol, row=currRow, columnspan=2)
    currRow += 1
    
    newEntry, newLabel = create_label_entry(newFrame, "Enter the name of this thing: ", projectName)
    newLabel.grid(column=currCol, row=currRow)
    currCol += 1
    newEntry.grid(column=currCol, row=currRow)
    currCol, currRow = 0, currRow + 1
    
    newCheckBox = create_check_box_label(newFrame, "This is a competition.", hasEvent)
    newCheckBox.grid(column=currCol, row=currRow, columnspan=2)
    currRow += 1
    
    newEntry, newLabel = create_label_entry(newFrame, "Enter the event's name: ", eventName)
    newLabel.grid(column=currCol, row=currRow)
    currCol += 1
    newEntry.grid(column=currCol, row=currRow)
    currCol, currRow = 0, currRow + 1
    
    newLabel, newComboBox, newLabel2, newComboBox2 = create_spin_month_year(newFrame, "Enter the month the thing took place:", monthEvent, yearEvent, yearsList)
    newLabel.grid(column=currCol, row=currRow)
    currCol += 1
    newComboBox.grid(column=currCol, row=currRow)
    currCol, currRow = 0, currRow + 1
    
    newLabel2.grid(column=currCol, row=currRow)
    currCol += 1
    newComboBox2.grid(column=currCol, row=currRow)
    currCol, currRow = 0, currRow + 1
    
    newLabel, projectDetailsText = create_label_text_field(newFrame, "Enter the details of this event: ", "projectDetailsText")
    newLabel.grid(column=currCol, row=currRow)
    currCol += 1
    projectDetailsText.grid(column=currCol, row=currRow)
    currRow += 1
    
    # Add Project Button
    newButton = tk.Button(newFrame, text="Add Project", command=lambda: addNewProject(
        projectName.get(), hasEvent.get(), eventName.get(), monthEvent.get(), yearEvent.get(),
        make_list_from_text(projectDetailsText, "projectDetail")), name="btnSubmit")
    newButton.grid(column=currCol, row=currRow)
    
    return newFrame
