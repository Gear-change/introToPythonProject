import tkinter as tk
from tkinter import messagebox
from commontools2 import create_combo_set3, create_label_entry
def addNewCat(skillCatName, comboCont):
    global skillCatagorys
    global listCatagories
    skillNo = skillCatagorys.__len__()
    newSkillCat = {
        "skillCatagory":skillCatName,
        "skillCatNo":skillNo,
        "CatIsRelevent":True,
    }
    global itemList
    # Check if the skill already exists in skillCatagorys
    tempInt = 0
    existingSkill = next((skill for skill in skillCatagorys if skill['skillCatagory'] == skillCatName), None)
    if existingSkill:
        tempInt = 0
        for skill in userSkills:
            if skill['skillCatagory'] == skillCatName:
                break
            tempInt += 1
        # let user know about preexisting catagory
        messagebox.showinfo(
            title="Duplicate Skill Catagory Detected", 
            message="This skill catagory is in there already"
            )
            
    else:
        # Add the new skill if it doesn't exist
        userSkills.append(newSkillCat)
        #now to add it to the spinner
        listCatagories.append(skillCatName)
        comboCont.configure(textvariable=listCatagories)
        


def addNewSkill(skillName, skillYear):
    newSkill = {
        "skillName": skillName,
        "skillYears": skillYear,
        "isRelevent": True,
    }
    global userSkills
    global itemList

    # Check if the skill already exists in userSkills
    tempInt = 0
    existingSkill = next((skill for skill in userSkills if skill['skillName'] == skillName), None)
    if existingSkill:
        tempInt = 0
        for skill in userSkills:
            if skill["skillName"] == skillName:
                break
            tempInt += 1
        # Prompt for overwrite
        overwriteSkill = messagebox.askyesno(
            title="Duplicate Skill Detected", 
            message="This skill is in there, do you wish to overwrite it?"
            )
        if overwriteSkill:
            # Replace the existing skill with the new one, but we want to keep the others
            userSkills.pop(tempInt)
            userSkills.append(newSkill)
            
    else:
        # Add the new skill if it doesn't exist
        userSkills.append(newSkill)

def addSkillCatFrame(theWidget):
    root = tk.Tk()
    root.title("Create a New Skill Catagory")
    thisFrame = tk.Frame(root, name="newSklCatFrame")
    skillCatName = tk.StringVar(value="", name="skillCatName2")

    curRow = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill: ", skillCatName)
    newLabel.grid(column=0, row=curRow)
    newEntry.grid(column=1, row=curRow)
    curRow += 1
    btnSkillSubmit = tk.Button(
        thisFrame, 
        text="Add Skill Catagory", 
        command=lambda: addNewCat(
            newEntry.get(),
            theWidget
        ), 
        name="btnAddCatagory"
    )
    btnSkillSubmit.grid(column=0, row=curRow, columnspan=2)
    thisFrame.pack()
    

def skillFrame(parent, listSkill, listCats):
    global userSkills
    global skillCatagorys 
    skillCatagorys = listCats
    skillcatName = tk.StringVar(parent, name = "sklCatList")
    userSkills = listSkill
    thisFrame = tk.Frame(parent, name="sklFrame")
    skillName = tk.StringVar(value="Skill", name="skillName")

    # UI setup
    curRow = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill: ", skillName)
    newLabel.grid(column=0, row=curRow)
    newEntry.grid(column=1, row=curRow)
    global listCatagories
    listCatagories = list()
    for skillCat in skillCatagorys:
        listCatagories.append(skillCat.get("skillCatName"))
    curRow += 1
    catwidgetname = "thisWidget"
    newCombo, newLabel = create_combo_set3(thisFrame, "Enter how many years you have been using this skill: ", skillcatName, listCatagories, catwidgetname)
    newLabel.grid(column=0, row=curRow)
    newCombo.grid(column=1, row=curRow)
    
    curRow += 1
    btnSkillSubmit = tk.Button(
        thisFrame, 
        text="Add Skill", 
        command=lambda: 
            addNewSkill(
                skillName.get(),
                listCatagories.index(skillcatName.get())
            ),
        name="btnSubmit"
    )
    btnCallCatFrame = tk.Button(
        thisFrame,
        text="Make Catagories for skills",
        command=lambda: addSkillCatFrame(newCombo),
        name="skillCatFrameBut"
    )
    btnSkillSubmit.grid(column=0, row=curRow, columnspan=2)
    curRow += 1
    btnCallCatFrame.grid(column=0, row=curRow, columnspan=2)
    thisFrame.pack()

    return thisFrame
