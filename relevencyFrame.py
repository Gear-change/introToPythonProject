from commontools2 import *
import tkinter as tk
from tkinter import ttk
from EducationTabFrame import degreeToString

def setRelevency(boolVal, boolToSet):
    boolToSet = boolVal

def openRelevencyFrame(*args):
    #unpack arguments
    firstName, middleInitial, lastName, userLinkedin, userGithub, userPhone, userEmail, userWork, userEducation, userSkills, userProjects = args
    #create the main window
    rWindow = tk.tk()
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
    for work in userWork:
        thisWorkR = work.get("isRelevent")
        newCheckButton = ttk.Checkbutton(
            master=rFrame,
            command=setRelevency(thisWorkR, work["isRelevent"]),
            variable=thisWorkR,
            onvalue=True,
            offvalue=False,
            text=degreeToString(degree)
        )