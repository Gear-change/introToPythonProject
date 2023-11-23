from commontools2 import *
import tkinter as tk
from tkinter import ttk
from EducationTabFrame import degreeToString
from monthStringScript import monthToString
from makeResumeScript import makeResume

def CreateNewCheckButton(parent, thisBool, text):
    newCheckButton = ttk.Checkbutton(
        master=parent,
        variable=thisBool,
        onvalue=True,
        offvalue=False,
        text=text
    )
    return newCheckButton

def CreateNewRadioButton(parent, inValNum, inText, inVariable):
    newRadiobutton = ttk.Radiobutton(
        parent,
        value=inValNum,
        text=inText,
        variable=inVariable
    )
    return newRadiobutton

def projectToString(project):
    stringProject = ""
    stringProjectMain = ""
    if project.get("hasEvent"):
        #then is a compatition type of event
        stringProjectMain = project.get("eventName")+(": "+str((project.get("projectName"))))
    else:
        stringProjectMain = project.get ("projectName")
    stringProjectMonthYear = monthToString (project.get("month")) +  " - " + str(project.get("year"))
    stringProject = stringProjectMain + (", on "+(stringProjectMonthYear))
    return stringProject

def skillToString(skill):
    skillName = skill.get("skillName")
    skillYears = skill.get("skillYears")
    skillString = skillName+(" "+(str(skillYears)))
    return skillString

def workToString(work):
    companyName = work.get("companyName")
    companyStartM_Y = monthToString(work.get("dateStartMonth"))+(", ")+(str(work.get("dateStartYear")))
    companyEndM_Y = monthToString(work.get("dateEndMonth"))+(", ")+(str(work.get("dateEndYear")))
    outString = companyName+(" where you worked from ")+(companyStartM_Y)+(" to ")+(companyEndM_Y)
    return outString

def setRelevency(boolVal, boolToSet):
    boolToSet = boolVal

def openRelevencyFrame(*args):
    #unpack arguments
    global userWork
    global userSkills
    global userProjects
    global userEducation
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    #create the main window
    rWindow = tk.Tk()
    rWindow.title("Relevency window")
    rFrame = ttk.Frame(rWindow)
    rFrame.grid()
    curCol = 0
    curRow = 0
    ttk.Label(
        rFrame, 
        text="select the items that are relevent to the job you are applying to:"
        ).grid(column=curCol, row=curRow)
    curRow += 1
    for degree in userEducation:
        newCheckButton = CreateNewCheckButton(
            rFrame, 
            degree['isRelevent'], 
            degreeToString(degree)
            )
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        degreeDetailList = degree['degreeDetails']
        for detail in degreeDetailList:
            newCheckButton = CreateNewCheckButton(
                rFrame, 
                degree['isRelevent'], 
                detail.get("degreeDetail")
                )
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
        curRow += 1
    listTitlesRelevince = []
    for work in userWork:
        newTitleInt = tk.IntVar
        listTitlesRelevince.append(newTitleInt)
    intTemp = 0
    for work in userWork:
        newCheckButton = CreateNewCheckButton(
            rFrame,
            work['isRelevent'],
            workToString(work)+(" as :")
            )
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
        ttk.Label(
            rFrame,
            text="\t select the occupation title for this job you wish this employer to see:"
            ).grid(
                column=curCol,row=curRow
                )
        curRow += 1
        tempIntTwo = 0
        for title in work["occupationTitles"]:
            newRadioButton = CreateNewRadioButton(
                rFrame,
                title['titleNo'],
                title["OccupationTitle"],
                listTitlesRelevince[intTemp]
            )
            newRadioButton.grid(column=curCol, row=curRow)
            curRow += 1
            tempIntTwo += 1
        for detail in work["occupationDetails"]:
            newCheckButton = CreateNewCheckButton(
                rFrame, 
                detail["isRelevent"], 
                detail.get("OccupationDetail")
                )
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
        curRow += 1
        intTemp += 1
    curRow+=1
    for skill in userSkills:
        newCheckButton = CreateNewCheckButton(
            rFrame, 
            skill['isRelevent'],
            skillToString(skill)
            )
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
    curRow+=1
    for project in userProjects:
        newCheckButton = CreateNewCheckButton(
            rFrame,
            project["isRelevent"],
            projectToString(project)
        )
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
        for detail in project["projectDetails"]:
            newCheckButton = CreateNewCheckButton(
                rFrame,
                detail['isRelevent'],
                detail.get("projectDetail")
            )
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
    curRow+=1
    ttk.Label(
        rFrame, 
        text="Describe yourself to said employer:"
        ).grid(
            column=curCol, 
            row=curRow
            )
    userDesc = tk.StringVar()
    curRow+=1
    newEntry = tk.Entry(rFrame, textvariable=userDesc)
    newEntry.grid(column=curCol, row=curRow)
    curRow += 1
    newButton = tk.Button(
        rFrame,
        text="Make resume",
        command=lambda:setRelevenceyFinal(
            listTitlesRelevince, 
            userDesc, 
            firstName, 
            middleInitial, 
            lastName, 
            userLinkedin, 
            userGithub, 
            userPhone, 
            userEmail, 
            userWork, 
            userEducation, 
            userSkills, 
            userProjects
            )
    )
    newButton.grid(column=curCol, row=curRow)
    rFrame.mainloop()
def setRelevenceyFinal(dictTitlesRelevince, *args):
    #spool out the variables
    userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    #we need to set the titles that are and are not relevent,
    for (work, value) in (userWork, dictTitlesRelevince.values()):
        occupation = work["occupationTitles"]
        for title in occupation:
            if str(title["titleNo"]) == value:
                #then this is the title the user wants
                title["isRelevent"] = True
            else:
                #not the title the user wants
                title["isRelevent"] = False
    makeResume(
        userDesc.get(), 
        firstName.get(), 
        middleInitial.get(), 
        lastName.get(), 
        userLinkedin.get(), 
        userGithub.get(), 
        userPhone.get(), 
        userEmail.get(), 
        userWork, 
        userEducation, 
        userSkills, 
        userProjects
        )
    