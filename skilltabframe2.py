import tkinter as tk
from tkinter import messagebox
from commontools2 import create_combo_set3, create_label_entry

def addNewCat(skillCatName, comboCont):
    """
    Adds a new skill category to the list of skill categories if it doesn't already exist.
    Updates the dropdown menu (combo box) with the new category.
    
    Args:
        skillCatName (str): Name of the skill category to add.
        comboCont (tk.Widget): The combo box to update with the new category.
    """
    global skillCatagorys, listCatagories
    skillNo = len(skillCatagorys)
    
    # Check if the skill already exists in skillCatagorys
    existingSkill = next((skill for skill in skillCatagorys if skill['skillCatagory'] == skillCatName), None)
    if existingSkill:
        # Let user know about preexisting category
        messagebox.showinfo(
            title="Duplicate Skill Category Detected", 
            message="This skill category is already in the list."
        )
    else:
        # Add the new skill category if it doesn't exist
        newSkillCat = {
            "skillCatagory": skillCatName,
            "skillCatNo": skillNo,
            "CatIsRelevent": True,
        }
        skillCatagorys.append(newSkillCat)
        # Update the combo box with the new category
        listCatagories.append(skillCatName)
        comboCont.configure(values=listCatagories)

def addNewSkill(skillName, skillYear):
    """
    Adds a new skill to the list of user skills or updates an existing one.
    
    Args:
        skillName (str): Name of the skill to add or update.
        skillYear (int): Number of years the skill has been used.
    """
    newSkill = {
        "skillName": skillName,
        "skillYears": skillYear,
        "isRelevent": True,
    }
    global userSkills

    # Check if the skill already exists in userSkills
    existingSkill = next((skill for skill in userSkills if skill['skillName'] == skillName), None)
    if existingSkill:
        # Prompt for overwrite
        overwriteSkill = messagebox.askyesno(
            title="Duplicate Skill Detected", 
            message="This skill is already in the list. Do you wish to overwrite it?"
        )
        if overwriteSkill:
            # Replace the existing skill with the new one
            userSkills = [skill if skill['skillName'] != skillName else newSkill for skill in userSkills]
    else:
        # Add the new skill if it doesn't exist
        userSkills.append(newSkill)

def addSkillCatFrame(theWidget):
    """
    Opens a new window to add a new skill category.
    
    Args:
        theWidget (tk.Widget): The combo box to update with the new category.
    """
    root = tk.Tk()
    root.title("Create a New Skill Category")
    
    thisFrame = tk.Frame(root, name="newSklCatFrame")
    skillCatName = tk.StringVar(value="", name="skillCatName2")

    curRow = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill category: ", skillCatName)
    newLabel.grid(column=0, row=curRow)
    newEntry.grid(column=1, row=curRow)

    curRow += 1
    btnSkillSubmit = tk.Button(
        thisFrame, 
        text="Add Skill Category", 
        command=lambda: addNewCat(newEntry.get(), theWidget),
        name="btnAddCategory"
    )
    btnSkillSubmit.grid(column=0, row=curRow, columnspan=2)

    thisFrame.pack()

def skillFrame(parent, listSkill, listCats):
    """
    Creates the skill tab frame with UI elements for managing skills and categories.
    
    Args:
        parent (tk.Widget): The parent widget (tab).
        listSkill (list): The list of user skills.
        listCats (list): The list of skill categories.
    
    Returns:
        tk.Frame: The created frame for the skill tab.
    """
    global userSkills, skillCatagorys, listCatagories
    skillCatagorys = listCats
    userSkills = listSkill

    thisFrame = tk.Frame(parent, name="sklFrame")
    skillName = tk.StringVar(value="Skill", name="skillName")
    skillcatName = tk.StringVar(parent, name="sklCatList")

    curRow = 0
    newEntry, newLabel = create_label_entry(thisFrame, "Enter the name of the skill: ", skillName)
    newLabel.grid(column=0, row=curRow)
    newEntry.grid(column=1, row=curRow)

    listCatagories = [skillCat.get("skillCatagory") for skillCat in skillCatagorys]
    curRow += 1
    newCombo, newLabel = create_combo_set3(thisFrame, "Select the skill category: ", skillcatName, listCatagories)
    newLabel.grid(column=0, row=curRow)
    newCombo.grid(column=1, row=curRow)
    
    curRow += 1
    btnSkillSubmit = tk.Button(
        thisFrame, 
        text="Add Skill", 
        command=lambda: addNewSkill(skillName.get(), listCatagories.index(skillcatName.get())),
        name="btnSubmit"
    )
    btnSkillSubmit.grid(column=0, row=curRow, columnspan=2)

    curRow += 1
    btnCallCatFrame = tk.Button(
        thisFrame,
        text="Create Skill Categories",
        command=lambda: addSkillCatFrame(newCombo),
        name="skillCatFrameBut"
    )
    btnCallCatFrame.grid(column=0, row=curRow, columnspan=2)

    thisFrame.pack()

    return thisFrame
