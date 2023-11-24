import tkinter as tk
from tkinter import messagebox
from commontools2 import create_label_entry, create_combo_set

def addNewSkill(skillName, skillYear):
    newSkill = {
        "skillName": skillName,
        "skillYears": skillYear,
        "isRelevent": True,
    }
    global userSkills

    # Check if the skill already exists in userSkills
    existingSkill = next((skill for skill in userSkills if skill['skillName'] == skillName), None)
    if existingSkill:
        tempInt = 0
        for skill in userSkills:
            if skill["skillName"] == skillName:
                break
            tempint += 1
        # Prompt for overwrite
        overwriteSkill = messagebox.askyesno(title="Duplicate Skill Detected", 
                                             message="This skill is in there, do you wish to overwrite it?")
        if overwriteSkill:
            # Replace the existing skill with the new one, but we want to keep the others
            userSkills.pop(tempInt)
            userSkills.append(newSkill)
            
    else:
        # Add the new skill if it doesn't exist
        userSkills.append(newSkill)

def skillFrame(parent, listSkill):
    global userSkills
    userSkills = listSkill

    thisFrame = tk.Frame(parent)
    yearsList = list(range(100))
    skillName = tk.StringVar(value="Skill")
    skillYear = tk.IntVar(value=0)

    # UI setup
    curRow = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill: ", skillName)
    newLabel.grid(column=0, row=curRow)
    newEntry.grid(column=1, row=curRow)
    
    curRow += 1
    newCombo, newLabel = create_combo_set(thisFrame, "Enter how many years you have been using this skill: ", skillYear, yearsList)
    newLabel.grid(column=0, row=curRow)
    newCombo.grid(column=1, row=curRow)
    
    curRow += 1
    btnSkillSubmit = tk.Button(thisFrame, text="Add Skill", 
                               command=lambda: addNewSkill(skillName.get(), skillYear.get()))
    btnSkillSubmit.grid(column=0, row=curRow, columnspan=2)

    return thisFrame
