#https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/

import tkinter as tk                     
from tkinter import Entry, Grid, ttk 
def addNewDegree(DegreeType, DegreeField, degreeSubField,schoolAddress1, schoolCity, schoolAddress2, schoolState, SchoolDateEndMonth, SchoolDateEndYear, SchoolDateStartMonth, SchoolDateStartYear,GPA):
    global userEducation
    global genericEducation
    newEducation = genericEducation.copy()
    newEducation["degreeType"] = DegreeType
    newEducation["degreeField"] = DegreeField
    newEducation["degreeSubField"] = degreeSubField
    newEducation["schoolAddress1"] = schoolAddress1
    newEducation["schoolAddress2"] = schoolAddress2
    newEducation["gradeGPA"] = GPA
    newEducation["schoolCity"] = schoolCity
    newEducation["schoolState"] = schoolState
    newEducation["dateStartYear"] = SchoolDateStartYear
    newEducation["dateStartMonth"] = SchoolDateStartMonth
    newEducation["dateEndYear"] = SchoolDateEndYear
    newEducation["dateEndMonth"] = SchoolDateEndMonth

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
    root.title("Resume Generator") 
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
    DegreeType = ttk.Combobox(tab2, width = 27, textvariable = tk.StringVar() , values = [ ' Highschool',  ' Accociate', ' Bachelor', ' Master', ' Doctorate' ]).grid(column=currCol,row=currRow, columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="Degree Field: ").grid(column=currCol,row=currRow)
    currCol+=1
    DegreeField = Entry(tab2).grid(column=currCol,row=currRow)
    currCol = 4
    currRow +=1
    ttk.Label(tab2, text="Degree Subfield: ").grid(column=currCol,row=currRow)
    currCol+=1
    degreeSubField = Entry(tab2).grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    ttk.Label(tab2, text="Address of School: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolAddress1 = Entry(tab2).grid(column=currCol,row=currRow,columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="School City").grid(column=currCol,row=currRow)
    currCol+=1
    schoolCity = Entry(tab2).grid(column=currCol,row=currRow)
    currCol = 0
    currRow+=1
    ttk.Label(tab2, text="Address line 2:").grid(column=currCol,row=currRow)
    currCol+=1
    schoolAddress2 = Entry(tab2).grid(column=currCol,row=currRow,columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="School State: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolState = ttk.Combobox(tab2, width = 27, textvariable = tk.StringVar() , values = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']).grid(column=currCol,row=currRow)
    currRow += 1
    currCol = 0
    ttk.Label(tab2, text="Graduation date: ").grid(column=currCol,row=currRow)
    currCol += 1
    #date frame construct
    SchoolDateEndMonth = ttk.Combobox(tab2, width = 5, textvariable = tk.StringVar() , values = ['1','2','3','4','5','6','7','8','9','10','11','12']).grid(column=currCol,row=currRow)
    yearsList= []
    currCol +=1
    ttk.Label(tab2, text=" - ").grid(column=currCol,row=currRow)
    for x in range(1950,2050):
        yearsList.append(str(x))      
    currCol +=1  
    SchoolDateEndYear = ttk.Combobox(tab2, width = 5, textvariable = tk.StringVar() , values = yearsList).grid(column=currCol,row=currRow)
    currCol +=1
    ttk.Label(tab2, text="GPA: ").grid(column=currCol, row=currRow)
    currCol +=1
    GPA = Entry(tab2).grid(column=currCol,row=currRow)
    #date frame construct
    currRow += 1
    currCol = 0
    ttk.Label(tab2, text="Start date: ").grid(column=currCol,row=currRow)
    currCol +=1
    SchoolDateStartMonth = ttk.Combobox(tab2, width = 5, textvariable = tk.StringVar() , values = ['1','2','3','4','5','6','7','8','9','10','11','12']).grid(column=currCol,row=currRow)
    currCol +=1
    ttk.Label(tab2, text=" - ").grid(column=currCol,row=currRow)
    currCol +=1
    SchoolDateStartYear = ttk.Combobox(tab2, width = 5, textvariable = tk.StringVar(), values = yearsList).grid(column=currCol,row=currRow)
    #add the button to call the function to add an education
    currCol +=2
    btnSchoolSubmit = tk.Button(tab2, text="add Degree", command=addNewDegree(DegreeType, DegreeField, degreeSubField,schoolAddress1, schoolCity, schoolAddress2, schoolState, SchoolDateEndMonth, SchoolDateEndYear, SchoolDateStartMonth, SchoolDateStartYear,GPA))
    btnSchoolSubmit.grid(column=currCol,row=currRow)
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
    "degreeSubField":"",
    "schoolAddress1":"",
    "schoolAddress2":"",
    "gradeGPA":0,
    "schoolCity":"",
    "schoolState":"",
    "dateStartYear":0,
    "dateStartMonth":0,
    "dateEndYear":0,
    "dateEndMonth":0,
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