import tkinter as tk                     
from tkinter import Entry, Grid, ttk 

def degreeToString(degree):
    try:
        stringOut = degree.get("degreeType") + " in " + degree.get("degreeField") + ":" +("degreeSubField")
        return stringOut
    except:
        print("error degree")
        print(degree)
        return " "
    
global tab2
tab2 = None 
global DegreeFrame
DegreeFrame = tk.Frame(tab2)

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
    userEducation.append(newEducation)
    global DegreeFrame
    degreeNum = len(userEducation) - 1
    newCheckbox = tk.Checkbutton(DegreeFrame, text=degreeToString(newEducation),
                                     variable=userEducation[degreeNum], 
                                     onvalue=True,
                                     offvalue=False)
    newCheckbox.grid(column=0,row=degreeNum)
    newButton = tk.Button(DegreeFrame, text="delete degree", command=(userEducation.pop(degreeNum)))
    newButton.grid(column=1, row=degreeNum)

def mainApp():
    global firstName  
    global middleInitial
    global lastName
    global userLinkedin
    global userGithub
    global userPhone
    global userEmail
    global userDescription
    global userEducation
    global userWork
    global userSkills
    global userProjects
    #https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
    root = tk.Tk() 
    root.title("Resume Generator") 
    tabControl = ttk.Notebook(root) 
    global tab2
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
    ttk.Label(tab1, text ="Middle Initial: ").grid(row=currRow,column=0)
    middleInitial = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Last Name: ").grid(row=currRow,column=0)
    lastName = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Linkedin Profile: ").grid(row=currRow,column=0)
    userLinkedin = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Github Profile(optional): ").grid(row=currRow,column=0)
    userGithub = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Email: ").grid(row=currRow,column=0)
    userEmail = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    ttk.Label(tab1, text ="Email: ").grid(row=currRow,column=0)
    userEmail = Entry(tab1).grid(row=currRow,column=1)
    currRow += 1
    #this is tab1 done, now for tab2
    currCol = 0
    currRow = 0
    ttk.Label(tab2,text = "Degree type:").grid(column=currCol,row=currRow)
    currCol += 1
    #thanks:https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/?ref=lbp
    DegreeType = tk.StringVar()
    newcombo = ttk.Combobox(tab2, width = 27, textvariable = DegreeType , values = [ ' Highschool',  ' Accociate', ' Bachelor', ' Master', ' Doctorate' ])
    newcombo.grid(column=currCol,row=currRow, columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="Degree Field: ").grid(column=currCol,row=currRow)
    currCol+=1
    DegreeField = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=DegreeField )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 4
    currRow +=1
    ttk.Label(tab2, text="Degree Subfield: ").grid(column=currCol,row=currRow)
    currCol+=1
    degreeSubField = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=degreeSubField )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow += 1
    ttk.Label(tab2, text="Address of School: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolAddress1 = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=schoolAddress1 )
    newEntry.grid(column=currCol,row=currRow,columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="School City").grid(column=currCol,row=currRow)
    currCol+=1
    schoolCity = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=schoolCity )
    newEntry.grid(column=currCol,row=currRow)
    currCol = 0
    currRow+=1
    ttk.Label(tab2, text="Address line 2:").grid(column=currCol,row=currRow)
    currCol+=1
    schoolAddress2 = tk.StringVar()
    newEntry = Entry(tab2, width = 27, textvariable=schoolAddress2 )
    newEntry.grid(column=currCol,row=currRow,columnspan=3)
    currCol+=3
    ttk.Label(tab2, text="School State: ").grid(column=currCol,row=currRow)
    currCol+=1
    schoolState = tk.StringVar()
    newComboBox = ttk.Combobox(tab2, width = 27, textvariable = schoolState , values = [ 'Alabama',
                                                                                            'Alaska', 
                                                                                            'Arizona', 
                                                                                            'Arkansas',
                                                                                            'California',
                                                                                            'Colorado',
                                                                                            'Connecticut',
                                                                                            'Delaware',
                                                                                            'Florida',
                                                                                            'Georgia',
                                                                                            'Hawaii',
                                                                                            'Idaho',
                                                                                            'Illinois',
                                                                                            'Indiana',
                                                                                            'Iowa',
                                                                                            'Kansas',
                                                                                            'Kentucky',
                                                                                            'Louisiana',
                                                                                            'Maine',
                                                                                            'Maryland',
                                                                                            'Massachusetts',
                                                                                            'Michigan',
                                                                                            'Minnesota',
                                                                                            'Mississippi',
                                                                                            'Missouri',
                                                                                            'Montana',
                                                                                            'Nebraska',
                                                                                            'Nevada',
                                                                                            'New Hampshire',
                                                                                            'New Jersey',
                                                                                            'New Mexico',
                                                                                            'New York',
                                                                                            'North Carolina',
                                                                                            'North Dakota',
                                                                                            'Ohio',
                                                                                            'Oklahoma',
                                                                                            'Oregon',
                                                                                            'Pennsylvania',
                                                                                            'Rhode Island',
                                                                                            'South Carolina',
                                                                                            'South Dakota',
                                                                                            'Tennessee',
                                                                                            'Texas',
                                                                                            'Utah',
                                                                                            'Vermont',
                                                                                            'Virginia',
                                                                                            'Washington',
                                                                                            'West Virginia',
                                                                                            'Wisconsin',
                                                                                            'Wyoming'
                                                                                            ])
    newComboBox.grid(column=currCol,row=currRow)
    currRow += 1
    currCol = 0
    ttk.Label(tab2, text="Graduation date: ").grid(column=currCol,row=currRow)
    currCol += 1
    #date frame construct
    SchoolDateEndMonth = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateEndMonth , values = [1,2,3,4,5,6,7,8,9,10,11,12])
    newComboBox.grid(column=currCol,row=currRow)
    yearsList= []
    currCol +=1
    ttk.Label(tab2, text=" - ").grid(column=currCol,row=currRow)
    for x in range(1950,2050):
        yearsList.append(x)      
    currCol +=1  
    SchoolDateEndYear = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateEndYear , values = yearsList)
    newComboBox.grid(column=currCol,row=currRow)
    currCol +=1
    ttk.Label(tab2, text="GPA: ").grid(column=currCol, row=currRow)
    currCol +=1
    GPA = tk.DoubleVar()
    newEntry = Entry(tab2, width = 27, textvariable = GPA )
    newEntry.grid(column=currCol,row=currRow)
    #date frame construct
    currRow += 1
    currCol = 0
    ttk.Label(tab2, text="Start date: ").grid(column=currCol,row=currRow)
    currCol +=1
    SchoolDateStartMonth = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateStartMonth , values = [1,2,3,4,5,6,7,8,9,10,11,12])
    newComboBox.grid(column=currCol,row=currRow)
    currCol +=1
    ttk.Label(tab2, text=" - ").grid(column=currCol,row=currRow)
    currCol +=1
    SchoolDateStartYear = tk.IntVar()
    newComboBox = ttk.Combobox(tab2, width = 5, textvariable = SchoolDateStartYear, values = yearsList)
    newComboBox.grid(column=currCol,row=currRow)
    #add the button to call the function to add an education
    currCol +=2
    btnSchoolSubmit = tk.Button(tab2, 
                                text="add Degree", 
                                command=addNewDegree(DegreeType.get(), 
                                                     DegreeField.get(), 
                                                     degreeSubField.get(),
                                                     schoolAddress1.get(), 
                                                     schoolCity.get(), 
                                                     schoolAddress2.get(), 
                                                     schoolState.get(), 
                                                     SchoolDateEndMonth.get(), 
                                                     SchoolDateEndYear.get(), 
                                                     SchoolDateStartMonth.get(),
                                                     SchoolDateStartYear.get(),
                                                     GPA.get()))
    btnSchoolSubmit.grid(column=currCol,row=currRow)
    global DegreeFrame
    DegreeFrame = tk.Frame(tab2)
    if (len(userEducation) < 0):
        currCol =0
        currRow +=1
        #now to make the selection interface
        global degreeNum
        degreeNum = 0
        for degree in userEducation:
            newCheckbox = tk.Checkbutton(DegreeFrame, text=degreeToString(degree),
                                     variable=userEducation[degreeNum], 
                                     onvalue=True,
                                     offvalue=False)
            newCheckbox.grid(column=0,row=degreeNum)
            newButton = tk.Button(DegreeFrame, text="delete degree", command=(userEducation.pop(degreeNum)))
            newButton.grid(column=1, row=degreeNum)
            degreeNum += 1
        DegreeFrame.grid(column=currCol,row=currRow,columnspan=5)   
    root.mainloop()   
global genericEducation
global genericWork
global genericSkill
global genericProject
global firstName  
global middleInitial
global lastName
global userLinkedin
global userGithub
global userPhone
global userEmail
global userDescription
global userEducation
global userWork
global userSkills
global userProjects
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
    "companyCity":"",
    "occupationTitle":"",
    "occupationDetails":[{
        "OccupationDetail":"",
        "isRelevent":True
    }],
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
    "projectDetails":[{
        "OccupationDetail":"",
        "isRelevent":True
    }],
}
userEducation=[]
userWork = []
userProjects = []
userSkills = []
mainApp()