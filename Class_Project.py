#https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/

import tkinter as tk                     
from tkinter import Entry, Grid, ttk 

def mainApp():
    global firstName  
    global lastName
    global userAddressLine1
    global userAddressLine2
    global userCity
    global userState
    global userEmail
    global userDescription

    root = tk.Tk() 
    root.title("Tab Widget") 
    tabControl = ttk.Notebook(root) 
  
    tab1 = ttk.Frame(tabControl) 
    tab2 = ttk.Frame(tabControl) 
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='Personal Information') 
    tabControl.add(tab2, text ='Education')
    tabControl.add(tab3, text ='Work experience')
    tabControl.add(tab4, text ='Skills')
    tabControl.add(tab5, text ='Other')
    tabControl.add(tab6, text ='Output/print/load')
    tabControl.pack(expand = 1, fill ="both")
    #now that the tab structure is done, on to populating our first tab 
    currRow = 0
    ttk.Label(tab1, text ="enter your information below: ").grid(row=currRow)
    currRow += 1
    ttk.Label(tab1, text ="First Name: ").grid(row=currRow,column=0)
    firstName = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Last Name: ").grid(row=currRow,column=0)
    lastName = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Address line 1: ").grid(row=currRow,column=0)
    userAddressLine1 = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Address line 2: ").grid(row=currRow,column=0)
    userAddressLine2 = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="City: ").grid(row=currRow,column=0)
    userCity = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="State: ").grid(row=currRow,column=0)
    userState = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Email: ").grid(row=currRow,column=0)
    userEmail = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Describe yourself: ").grid(row=currRow,column=0)
    userDescription = Entry(tab1).grid(row=currRow,column=1)
    #this is tab1 done, now for tab2
    currCol = 0
    currRow = 0
    ttk.Label(tab2,text = "Degree type:").grid(column=currCol,row=currRow)
    currCol += 1
    #thanks:https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/?ref=lbp
    n = tk.StringVar() 
    DegreeType = ttk.Combobox(tab2, width = 27, textvariable = n, values = [ ' Highschool',  ' Accociate', ' Bachelor', ' Master', ' Doctorate' ]).grid(column=currCol,row=currRow)
    
    root.mainloop()   
global genericEducation
global genericWork
global genericSkill
global firstName  
global lastName
global userAddressLine1
global userAddressLine2
global userCity
global userState
global userEmail
global userDescription
global userEducation
global userWork
global userSkills
global userProjects
genericEducation = {
    "degreeType":"",
    "degreeField":"",
    "SchoolType":"",
    "degreeSubField":"",
    "schoolAddress1":"",
    "gradeGPA":0,
    "schoolCity":"",
    "schoolState":"",
    "dateStart":"",
    "dateEnd":"",
    "isRelevent":True
}
genericWork = {
    "companyName":"",
    "companyAddress":"",
    "companyPhone":"",
    "bossName":"",
    "supervisorName":"",
    "occupation":"",
    "workStart":"",
    "workFinish":"",
    "reasonForEnd":"",
    "isRelevent":True,
}
genericSkill = {
    "skillName":"",
    "skillYears":"",
    "isRelevent":True,
}
userEducation=[]
userWork = []
userProjects = []
userSkills = []
mainApp()