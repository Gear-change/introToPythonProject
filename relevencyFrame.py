from commontools2 import *
import tkinter as tk
from tkinter import ttk
from EducationTabFrame import degreeToString
from monthStringScript import monthToString
from makeResumeScript import makeResume

def projectToString(project):
    stringProject = ""
    stringProjectMain = ""
    if project.get("hasEvent"):
        #then is a compatition type of event
        stringProjectMain = project.get("eventName").join(": ".join(project.get("projectName")))
    else:
        stringProjectMain = project.get("projectName")
    stringProjectMonthYear = monthToString(project.get("month")).join(
        " - ".join(project.get("year"))
    )
    stringProject = stringProjectMain.join(
        ", on ".join(
            stringProjectMonthYear
        )
    )
    return stringProject

def skillToString(skill):
    skillName = skill.get("skillName")
    skillYears = skill.get("skillYears")
    skillString = skillName.join(" ".join(str(skillYears)))
    return skillString

def workToString(work):
    companyName = work.get("companyName")
    companyStartM_Y = monthToString(work.get("dateStartMonth")).join(", ").join(str(work.get("dateStartYear")))
    companyEndM_Y = monthToString(work.get("dateEndMonth")).join(", ").join(str(work.get("dateEndYear")))
    outString = companyName.join(" where you worked from ").join(companyStartM_Y).join(" to ").join(companyEndM_Y)
    return outString

def setRelevency(boolVal, boolToSet):
    boolToSet = boolVal

def openRelevencyFrame(*args):
    #unpack arguments
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    #create the main window
    rWindow = tk.Tk()
    rWindow.title("Relevency window")
    rFrame = ttk.Frame(rWindow)
    rFrame.grid()
    curCol = 0
    curRow = 0
    ttk.Label(rFrame, text="select the items that are relevent to the job you are applying to:").grid(column=curCol, row=curRow)
    curRow += 1
    for degree in userEducation:
        thisDegreeR = degree.get('isRelevent')
        newCheckButton = ttk.Checkbutton(
            master=rFrame,
            command=setRelevency(thisDegreeR, degree["isRelevent"]),
            variable=thisDegreeR,
            onvalue=True,
            offvalue=False,
            text=degreeToString(degree)
        )
        newCheckButton.grid(column=curCol, row=curRow)
        curRow += 1
        degreeDetailList = degree.get('degreeDetails')
        for detail in degreeDetailList:
            thisDetailR = detail.get("isRelevent")
            newCheckButton = ttk.Checkbutton(
                master=rFrame,
                command=setRelevency(thisDetailR, degree["isRelevent"]),
                variable=thisDetailR,
                onvalue=True,
                offvalue=False,
                text=detail.get("degreeDetail")
            )
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
        curRow += 1
    dictTitlesRelevince = {}
    intTemp = 0
    for work in userWork:
        workVarString =str(intTemp)
        intTemp += 1
        dictTitlesRelevince.update({
            workVarString:tk.IntVar
        })
    intTemp = 0
    for work in userWork:
        thisWorkR = work.get("isRelevent")
        newCheckButton = ttk.Checkbutton(
            master=rFrame,
            command=lambda:setRelevency(thisWorkR, work["isRelevent"]),
            variable=thisWorkR,
            onvalue=True,
            offvalue=False,
            text=workToString(work).join(" as :")
        ).grid(column=curCol,row=curRow)
        curRow += 1
        ttk.Label(
            rFrame,
            text="\t select the occupation title for this job you wish this employer to see:"
            ).grid(
                column=curCol,row=curRow
                )
        curRow += 1
        for title in work["occupationTitles"]:
            ttk.Radiobutton(
                rFrame,
                text=title["OccupationTitle"],
                value=title["titleNo"],
                variable=dictTitlesRelevince[str(intTemp)]
            ).grid(column=curCol,row=curRow)
            curRow+=1
        for detail in work["occupationDetails"]:
            thisDetailR = detail.get("isRelevent")
            newCheckButton = ttk.Checkbutton(
                master=rFrame,
                command=lambda:setRelevency(thisDetailR, degree["isRelevent"]),
                variable=thisDetailR,
                onvalue=True,
                offvalue=False,
                text=detail.get("degreeDetail")
            )
            newCheckButton.grid(column=curCol,row=curRow)
            curRow += 1
        curRow += 1
        intTemp += 1
    curRow+=1
    for skill in userSkills:
        thisSkillR = skill["isRelevent"]
        skillString = skillToString(skill)
        newCheckButton = ttk.Checkbutton(
            rFrame,
            command=lambda:setRelevency(thisSkillR, skill["isRelevent"]),
            variable=thisSkillR,
            onvalue=True,
            offvalue=False,
            text=skillString
        )
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
    curRow+=1
    for project in userProjects:
        thisProjectR = project["isRelevent"]
        projectString = projectToString(project)
        newCheckButton = ttk.Checkbutton(
            rFrame,
            command=lambda:setRelevency(thisProjectR, project["isRelevent"]),
            variable=thisProjectR,
            onvalue=True,
            offvalue=False,
            text=projectString
        )
        newCheckButton.grid(column=curCol,row=curRow)
        curRow += 1
    curRow+=1
    ttk.Label(rFrame, text="Describe yourself to said employer:")
    userDesc = tk.StringVar()
    newEntry = tk.Entry(rFrame, textvariable=userDesc)
    newEntry.grid(column=curCol, row=curRow)
    newButton = tk.Button(
        rFrame,
        text="Make resume",
        command=lambda:setRelevenceyFinal(dictTitlesRelevince, userDesc, *args)
    )
    newButton.grid(column=curCol, row=curRow)
    newList = dictTitlesRelevince.values()
    print(newList)
def setRelevenceyFinal(dictTitlesRelevince, *args):
    #spool out the variables
    userDesc, firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    #we need to set the titles that are and are not relevent,
    for [work, value] in [userWork, dictTitlesRelevince.values()]:
        for title in work["occupationTitles"]:
            if str(title["titleNo"]) == value:
                #then this is the title the user wants
                title["isRelevent"] = True
            else:
                #not the title the user wants
                title["isRelevent"] = False
    makeResume(*args)
    