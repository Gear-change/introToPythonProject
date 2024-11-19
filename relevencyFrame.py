from commontools2 import *
import tkinter as tk
from tkinter import ttk
from EducationTabFrame import degreeToString
from monthStringScript import monthToString
from makeResumeScript import makeResume, makeText
from VerticalScrolledFrame import VerticalScrolledFrame

def setFlag(aVar, var):
    """
    Sets the value of a variable to the value of another variable.
    
    Args:
        aVar: The source variable.
        var: The target variable.
    """
    var = aVar.get()

def CreateNewCheckButton(parent, thisBool, text, uid):
    """
    Creates a new check button.
    
    Args:
        parent (tk.Widget): The parent widget.
        thisBool (bool): The initial value of the check button.
        text (str): The text displayed by the check button.
        uid (str): The unique identifier for the check button.
    
    Returns:
        ttk.Checkbutton: The created check button.
    """
    def setFlag(aVar, var):
        var = aVar.get()
    thisBoolVar = tk.BooleanVar(parent, thisBool, str(uid))
    newCheckButton = ttk.Checkbutton(
        master=parent,
        command=setFlag(thisBoolVar,thisBool),
        variable=thisBoolVar,
        onvalue=True,
        offvalue=False,
        text=text
    )
    return newCheckButton

def skillCatToString(catagory):
    """
    Converts a skill category dictionary to a string representation.
    
    Args:
        catagory (dict): The skill category information.
    
    Returns:
        str: The string representation of the skill category.
    """
    return catagory.get("skillCatagory")

def projectToString(project):
    """
    Converts a project dictionary to a string representation.
    
    Args:
        project (dict): The project information.
    
    Returns:
        str: The string representation of the project.
    """
    if project.get("hasEvent"):
        project_main = f"{project['eventName']}: {project['projectName']}"
    else:
        project_main = project['projectName']
    project_date = f"{monthToString(project['month'])} - {project['year']}"
    return f"{project_main}, on {project_date}"

def skillToString(skill):
    """
    Converts a skill dictionary to a string representation.
    
    Args:
        skill (dict): The skill information.
    
    Returns:
        str: The string representation of the skill.
    """
    return skill.get("skillName")

def workToString(work):
    """
    Converts a work experience dictionary to a string representation.
    
    Args:
        work (dict): The work experience information.
    
    Returns:
        str: The string representation of the work experience.
    """
    company_name = work.get("companyName")
    start_date = f"{monthToString(work.get('dateStartMonth'))}, {work.get('dateStartYear')}"
    end_date = f"{monthToString(work.get('dateEndMonth'))}, {work.get('dateEndYear')}"
    return f"{company_name} where you worked from {start_date} to {end_date}"

def setRelevency(boolVal, boolToSet):
    """
    Sets the relevancy of a boolean variable.
    
    Args:
        boolVal (bool): The value to set.
        boolToSet (bool): The target variable.
    """
    boolToSet = boolVal


def openRelevencyFrame(*args):
    """
    Opens a frame for selecting relevancy of resume items.
    
    Args:
        *args: The user data and settings.
    """
    global userWork, userSkills, userProjects, userEducation
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories = args

    # Create the main window
    rWindow = tk.Tk()
    rWindow.title("Relevancy Window")
    rFrame = ttk.Frame(rWindow)
    newScrollableFrame = VerticalScrolledFrame(rFrame)
    rMainFrame = tk.Frame(newScrollableFrame.interior)
    rFrame.grid()

    curCol, curRow, curUID = 0, 0, 0
    
    # User file name entry
    ttk.Label(rMainFrame, text='Type in the name you want for the PDF:').grid(column=curCol, row=curRow)
    curRow += 1
    userFileName = tk.StringVar(rMainFrame)
    tk.Entry(rMainFrame, textvariable=userFileName).grid(column=curCol, row=curRow)
    curRow += 1

    # User description entry
    ttk.Label(rMainFrame, text="Describe yourself to your prospective employer:").grid(column=curCol, row=curRow)
    curRow += 1
    userDesc = tk.Text(rMainFrame, height=5, width=100)
    userDesc.grid(column=curCol, row=curRow)
    curRow += 1

    # Relevancy selection
    ttk.Label(rMainFrame, text="Select the items that are relevant to the job you are applying to:").grid(column=curCol, row=curRow)
    curRow += 1

    # Education details
    for degree in userEducation:
        newCheckButton = CreateNewCheckButton(rMainFrame, degree['isRelevent'], degreeToString(degree), curUID)
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        degreeDetailFrame = tk.Frame(rMainFrame)
        degreeDetailFrame.grid(column=curCol, row=curRow)
        aCol, aRow = 0, 0
        for detail in degree['degreeDetails']:
            newCheckButton = CreateNewCheckButton(degreeDetailFrame, detail['isRelevent'], detail.get("degreeDetail"), curUID)
            curUID += 1
            newCheckButton.grid(column=aCol, row=aRow)
            aRow += 1
        curRow += 1

    # Work details
    for work in userWork:
        newCheckButton = CreateNewCheckButton(rMainFrame, work['isRelevent'], workToString(work) + " as :", curUID)
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        ttk.Label(rMainFrame, text="Select the occupation title for this job you wish this employer to see:").grid(column=curCol, row=curRow)
        curRow += 1
        for title in work["OccupationTitle"]:
            newRadioButton = CreateNewCheckButton(rMainFrame, title["isRelevent"], title.get("OccupationTitle"), curUID)
            curUID += 1
            newRadioButton.grid(column=curCol, row=curRow)
            curRow += 1
        for detail in work["occupationDetails"]:
            newCheckButton = CreateNewCheckButton(rMainFrame, detail["isRelevent"], detail.get("OccupationDetail"), curUID)
            curUID += 1
            newCheckButton.grid(column=curCol, row=curRow)
            curRow += 1
        curRow += 1

    # Skill details
    for skill in userSkills:
        newCheckButton = CreateNewCheckButton(rMainFrame, skill['isRelevent'], skillToString(skill), curUID)
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1

    # Skill category details
    for category in userCatagories:
        newCheckButton = CreateNewCheckButton(rMainFrame, category["CatIsRelevent"], skillCatToString(category), curUID)
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1

    # Project details
    for project in userProjects:
        newCheckButton = CreateNewCheckButton(rMainFrame, project["isRelevent"], projectToString(project), curUID)
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        for detail in project["projectDetails"]:
            newCheckButton = CreateNewCheckButton(rMainFrame, detail['isRelevent'], detail["projectDetail"], curUID)
            curUID += 1
            newCheckButton.grid(column=curCol, row=curRow)
            curRow += 1

    # Create resume buttons
    curRow += 1
    tk.Button(
        rMainFrame,
        text="Make resume",
        command=lambda: setupChronology(rWindow, userFileName.get(), userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories, pdfCheck=True)
    ).grid(column=curCol, row=curRow)
    curRow += 1
    tk.Button(
        rMainFrame,
        text="Make resume",
        command=lambda: setupChronology(rWindow, userFileName.get(), userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories, pdfCheck=False)
    ).grid(column=curCol, row=curRow)
    
    newScrollableFrame.configure(height=500)
    rMainFrame.pack()
    newScrollableFrame.pack()
    rFrame.mainloop()

def setRelevenceyFinal(*args):
    """
    Finalizes the relevancy settings and generates the resume.
    
    Args:
        *args: The user data and settings.
    """
    rFrame, userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories, pdfCheck = args
    if pdfCheck:
        makeResume(
            rFrame, userFileName, userDesc.get("1.0", "end-1c"), firstName.get(), middleInitial.get(), lastName.get(),
            userLinkedin.get(), userGithub.get(), userPhone.get(), userEmail.get(), userWork, userEducation, userSkills, userProjects, userCatagories
        )
    else:
        makeText(
            rFrame, userFileName, userDesc.get("1.0", "end-1c"), firstName.get(), middleInitial.get(), lastName.get(),
            userLinkedin.get(), userGithub.get(), userPhone.get(), userEmail.get(), userWork, userEducation, userSkills, userProjects, userCatagories
        )

def setupChronology(*args):
    """
    Sorts the user data chronologically and finalizes the relevancy settings.
    
    Args:
        *args: The user data and settings.
    """
    rFrame, userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories, pdfCheck = args
    userWork.sort(key=lambda d: d["dateEndYear"], reverse=True)
    userEducation.sort(key=lambda d: d["dateEndYear"], reverse=True)
    userProjects.sort(reverse=True, key=lambda d: d["year"])
    setRelevenceyFinal(
        rFrame, userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects, userCatagories, pdfCheck
    )
