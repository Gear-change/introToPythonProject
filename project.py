import tkinter as tk
from tkinter import ttk
from EducationTabFrame import makeEducationTabFrame
from ProjectTabFrame import makeOtherTab
from personalInfoTab import makePersonalInformationtab
from workTabFrame import WorkFrame
from skilltabframe2 import skillFrame
from settings_tab_frame import make_settings_tab

def mainApp():
    """
    Initializes and runs the main application. This function sets up the tkinter GUI for 
    the Resume Generator, including tabs for personal information, education, work experience, 
    skills, projects, and settings. Each tab contains relevant GUI components.
    """
    global root
    root = tk.Tk()
    root.title("Resume Generator")
    
    # Initialize the tab control
    tabControl = ttk.Notebook(root)

    # Create and add tabs to the tab control
    tab_labels = ['Personal Information', 'Education', 'Work experience', 'Skills', 'Other', 'Output/print/load']
    tabs = [ttk.Frame(tabControl) for _ in tab_labels]
    for tab, label in zip(tabs, tab_labels):
        tabControl.add(tab, text=label)
    
    tabControl.pack(expand=1, fill="both")

    # Create user input variables
    user_info_vars = {
        'firstName': tk.StringVar(),
        'middleInitial': tk.StringVar(),
        'lastName': tk.StringVar(),
        'userLinkedin': tk.StringVar(),
        'userGithub': tk.StringVar(),
        'userPhone': tk.StringVar(),
        'userEmail': tk.StringVar()
    }

    # Initialize frames for each tab
    frames = [
        makePersonalInformationtab(tabs[0], **user_info_vars),
        makeEducationTabFrame(tabs[1], userEducation),
        WorkFrame(tabs[2], userWork),
        skillFrame(tabs[3], userSkills, skillCatagorys),
        makeOtherTab(tabs[4], userProjects),
        make_settings_tab(
            tabs[5], 
            user_info_vars['firstName'], user_info_vars['middleInitial'], 
            user_info_vars['lastName'], user_info_vars['userLinkedin'], 
            user_info_vars['userGithub'], user_info_vars['userPhone'], 
            user_info_vars['userEmail'], userWork, userEducation, userSkills, 
            userProjects, skillCatagorys
        )
    ]

    # Add frames to respective tabs
    for frame in frames:
        frame.grid(column=0, row=0)

    # Run the main loop
    root.mainloop()

# Global Variables
global userWork, userEducation, userSkills, userProjects, skillCatagorys
skillCatagorys = []
userWork = []
userEducation = []
userSkills = []
userProjects = []

# Generic structures for initializing user data
genericEducation = {
    "degreeType": "", "degreeField": "", "degreeMinor": "",
    "gradeGPA": 0, "schoolName": "", "schoolCity": "", "schoolState": "",
    "dateEndYear": 0, "dateEndMonth": 0, "isRelevent": True,
    "degreeDetails": [{"degreeDetail": "", "isRelevent": True}],
}
genericWork = {
    "companyName": "", "companyCity": "", "companyState": "",
    "OccupationTitle": [{"OccupationTitle": "", "isRelevent": True, "titleNo": 0}],
    "occupationDetails": [{"OccupationDetail": "", "isRelevent": True}],
    "isRelevent": True, "dateEndYear": 0, "dateEndMonth": 0,
    "dateStartYear": 0, "dateStartMonth": 0,
}
genericSkillCat = {"skillCatagory": "", "skillCatNo": 0, "CatIsRelevent": True}
genericSkill = {"skillName": "", "skillYears": 0, "isRelevent": True}
genericProject = {
    "projectName": "", "hasEvent": True, "eventName": "", 
    "month": 0, "year": 0, "isRelevent": True,
    "projectDetails": [{"projectDetail": "", "isRelevent": True}],
}

# Run the main application
mainApp()
