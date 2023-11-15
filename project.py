import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from EducationTabFrame import makeEducationTabFrame
from ProjectTabFrame import makeOtherTab
from personalInfoTab import makePersonalInformationtab
from workTabFrame import WorkFrame
from skillTabFrame import skillFrame
from SettingsTabFrame import makeSettingsTab

def mainApp():
    root = tk.Tk()
    root.title("Resume Generator")
    tabControl = ttk.Notebook(root)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)

    # ... Create other tabs ...

    tabControl.add(tab1, text='Personal Information')
    tabControl.add(tab2, text='Education')
    tabControl.add(tab3, text ='Work experience')
    tabControl.add(tab4, text ='Skills')
    tabControl.add(tab5, text ='Other')
    tabControl.add(tab6, text ='Output/print/load')

    # ... Add other tabs ...

    tabControl.pack(expand=1, fill="both")

    # Personal Information Tab
    firstName = tk.StringVar()
    middleInitial = tk.StringVar()
    lastName = tk.StringVar()
    userLinkedin = tk.StringVar()
    userGithub = tk.StringVar()
    userPhone = tk.StringVar()
    userEmail = tk.StringVar()
    PIFrame = makePersonalInformationtab(
        tab1, firstName, middleInitial, lastName, userLinkedin, 
        userGithub, userPhone, userEmail
    )
    PIFrame.grid(column=0,row=0)

    # ... Add other personal information entries ...
    
    # Education Tab

    newFrame = makeEducationTabFrame(tab2, userEducation)
    newFrame.grid(column=0,row=0)

    # work tab

    newFrame = WorkFrame(tab3, userWork)
    newFrame.grid(column=0, row=0)

    #skill tab
    
    newFrame = skillFrame(tab4, userSkills)
    newFrame.grid(column=0, row=0)

    #projectTab

    newFrame = makeOtherTab(tab5, userProjects)
    newFrame.grid(column=0, row=0)

    # ... Now the fun begins.
    newFrame = makeSettingsTab(
        tab6, firstName, middleInitial, lastName, userLinkedin, userGithub, 
        userPhone, userEmail, userWork, userEducation, userSkills, userProjects
    )
    newFrame.grid(column=0, row=0)

    # ... Other GUI elements ...

    root.mainloop()

# Global Variables
global userWork
global userEducation
global userSkills
global userProjects
userWork = []
userEducation = []
userSkills = []
userProjects = []
genericEducation = {
    "degreeType":"",
    "degreeField":"",
    "degreeMinor":"",
    "gradeGPA":0,
    "schoolName":"",
    "schoolCity":"",
    "schoolState":"",
    "dateEndYear":0,
    "dateEndMonth":0,
    "isRelevent":True,
    "degreeDetails":[
        {
            "degreeDetail":"",
            "isRelevent":True
        }
    ],
}
genericWork = {
    "companyName":"",
    "companyCity":"",
    "companyState":"",
    "occupationTitles":[{
        "OccupationTitle":"",
        "isRelevent":True
    }],
    "occupationDetails":[{
        "OccupationDetail":"",
        "isRelevent":True
    }],
    #is relevent should only make them sorted between them for only this one, the other ones don't print if it is not relevent.
    "isRelevent":True,
    "dateEndYear":0,
    "dateEndMonth":0,
    "dateStartYear":0,
    "dateStartMonth":0,
}
genericSkill = {
    "skillName":"",
    "skillYears":"",
    "isRelevent":True,
}
genericProject = {
    "projectName":"",
    "hasEvent":True,
    "eventName":"",
    "month":0,
    "year":0,
    "isRelevent":True,
    "projectDetails":[{
        "projectDetail":"",
        "isRelevent":True
    }],
}
# ... Other generic structures ...

mainApp()

