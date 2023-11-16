import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from commontools2 import create_label_entry, create_combo_set

def addNewSkill(skillName, skillYear):
    newSkill = {
        "skillName":skillName,
        "skillYears":skillYear,
        "isRelevent":True,
    }
    global userSkills
    if newSkill in userSkills:
        newAlert = messagebox(None, title="duplicate skill", detail="duplicate skill detected")
        newAlert.show()
    else:
        userSkills.append(newSkill)
    

def skillFrame(parent, listSkill):
    global userSkills
    userSkills = listSkill
    # ... Declare other StringVar or IntVar variables ...
    thisFrame = tk.Frame(parent)
    yearsList = [year for year in range(0, 100)]
    skillName = tk.StringVar()
    skillYear = tk.IntVar()

    #setting default for auto population

    skillName.set("Skill")
    skillYear.set(0)

    # ... Populateing skills Tab with labels, entries, comboboxes ...
    curRow = 0
    curCol = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill: ", 
                                          skillName)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newEntry.grid(column=curCol, row=curRow)
    curCol =0
    curRow += 1
    newCombo, newLabel = create_combo_set(thisFrame,"enter how many years you have been using this skill: ", skillYear, yearsList)
    newLabel.grid(column=curCol, row=curRow)
    curCol += 1
    newCombo.grid(column=curCol, row=curRow)
    curRow += 1
    # Add Skill Button
    btnSchoolSubmit = tk.Button(thisFrame, text="Add Degree", 
                                command=lambda:addNewSkill(skillName.get(), 
                                                            skillYear.get(),)) # Add other .get() calls
    btnSchoolSubmit.grid(column=curCol, row=curRow)
    return thisFrame