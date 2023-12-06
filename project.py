import tkinter as tk
from tkinter import ttk
from EducationTabFrame import makeEducationTabFrame
from ProjectTabFrame import makeOtherTab
from personalInfoTab import makePersonalInformationtab
from workTabFrame import WorkFrame
from skilltabframe2 import skillFrame
from settings_tab_frame import make_settings_tab
import pip

def install(package):
    """
    Install a package using pip. If pip has a 'main' attribute, use that, 
    otherwise use '_internal.main'. This function is used to ensure that 
    required packages are installed.

    Args:
    package (str): The name of the package to install.
    """
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def mainApp():
    """
    Initializes and runs the main application. This function sets up the tkinter GUI for 
    the Resume Generator, including tabs for personal information, education, work experience, 
    skills, projects, and settings. Each tab contains relevant GUI components.
    """
    global root
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

    newFrame = make_settings_tab(
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
    "OccupationTitle":[{
        "OccupationTitle":"",
        "isRelevent":True,
        "titleNo":0
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
    "skillYears":0,
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
# ... Other generic structures ....

#instal fpdf2
if __name__ == '__main__':
    install('fpdf2')
mainApp()

