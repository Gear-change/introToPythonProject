from commontools2 import *
import tkinter as tk
from tkinter import ttk
from EducationTabFrame import degreeToString
from monthStringScript import monthToString
from makeResumeScript import makeResume
def setFlag(aVar, var):
        var = aVar.get()
def CreateNewCheckButton(parent, thisBool, text, uid):
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
    curUID = 0
    ttk.Label(
        rFrame, 
        text="select the items that are relevent to the job you are applying to:"
        ).grid(column=curCol, row=curRow)
    curRow += 1
    for degree in userEducation:
        newCheckButton = CreateNewCheckButton(
            rFrame, 
            degree['isRelevent'], 
            degreeToString(degree),
            curUID
            )
        curUID += 1
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        degreeDetailFrame = tk.Frame(rFrame)
        degreeDetailFrame.grid(column=curCol,row=curRow)
        aCol = 0
        aRow = 0
        degreeDetailList = degree['degreeDetails']
        for detail in degreeDetailList:
            newCheckButton = CreateNewCheckButton(
                degreeDetailFrame, 
                degree['isRelevent'], 
                detail.get("degreeDetail"),
                curUID
                )
            curUID += 1
            newCheckButton.grid(column=aCol,row=aRow)
            aRow += 1
        curRow += 1
    for work in userWork:
        newCheckButton = CreateNewCheckButton(
            rFrame,
            work['isRelevent'],
            workToString(work)+(" as :"),
            curUID
            )
        curUID += 1
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
            newRadioButton = CreateNewCheckButton(
                rFrame,
                title["isRelevent"],
                detail.get("OccupationTitle"),
                curUID
            )
            curUID += 1
            newRadioButton.grid(column=curCol, row=curRow)
            curRow += 1
            tempIntTwo += 1
        for detail in work["occupationDetails"]:
            newCheckButton = CreateNewCheckButton(
                rFrame, 
                detail["isRelevent"], 
                detail.get("OccupationDetail"),
                curUID
                )
            curUID += 1
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
        curRow += 1
        intTemp += 1
    curRow+=1
    for skill in userSkills:
        newCheckButton = CreateNewCheckButton(
            rFrame, 
            skill['isRelevent'],
            skillToString(skill),
            curUID
            )
        curUID += 1
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
    curRow+=1
    for project in userProjects:
        newCheckButton = CreateNewCheckButton(
            rFrame,
            project["isRelevent"],
            projectToString(project),
            curUID
        )
        curUID += 1
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
        for detail in project["projectDetails"]:
            newCheckButton = CreateNewCheckButton(
                rFrame,
                detail['isRelevent'],
                detail["projectDetail"],
                curUID
            )
            curUID += 1
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
    curRow+=1
    userDesc = tk.Text(rFrame, height= 5, width=100,)
    userDesc.grid(column=curCol, row=curRow)
    curRow += 1
    ttk.Label(
        rFrame, 
        text='type in the name you want for the pdf:'
        ).grid(
            column=curCol,
            row=curRow
            )
    curRow += 1
    userFileName = tk.StringVar()
    newEntry = tk.Entry(rFrame, textvariable=userFileName)
    newEntry.grid(column=curCol,row=curRow)
    curRow += 1
    newButton = tk.Button(
        rFrame,
        text="Make resume",
        command=lambda:setRelevenceyFinal(
            userFileName,
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
def setRelevenceyFinal(*args):
    #spool out the variables
    userFileName, userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    makeResume(
        userFileName.get(),
        userDesc.get("1.0", "end-1c"), 
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
    